from flask import Flask, request, jsonify
from flask_cors import CORS
from controllers import chars
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Raccoon City, home of the Umbrella Corporation"})

@app.route('/chars', methods=["GET", "POST"])
def chars_handler():
    functions = {
        'GET': chars.index,
        "POST": chars.create
    }
    resp, code = functions[request.method](request)
    return jsonify(resp), code

@app.route("/chars/<int:char_id>", methods=["GET", "PUT", "DELETE"])
def char_handler(char_id):
    functions = {
        "GET": chars.show,
        "PUT": chars.update,
        "DELETE": chars.destroy
    }
    resp, code = functions[request.method](request, char_id)
    return jsonify(resp), code

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'WARNING! {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'WARNING! {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"Umbrella system failure"}, 500

if __name__ == '__main__':
    app.run(debug=True)