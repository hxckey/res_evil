from flask import Flask, request, jsonify
from flask_cors import CORS
from controllers import res-evil

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return f'Welcome to Raccoon City, home of the Umbrella Corporation'

