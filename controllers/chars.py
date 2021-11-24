from werkzeug.exceptions import BadRequest

chars = [
    {"id": 1, "name": "Jill Valentine", "affiliation": ["STARS"], "debut": "Resident Evil, 1996"},
    {"id": 2, "name": "Chris Redfield", "affiliation": ["STARS"], "debut": "Resident Evil, 1996"},
    {"id": 3, "name": "Leon S. Kennedy", "affiliation": ["RCPD"], "debut": "Resident Evil 2, 1998"},
    {"id": 4, "name": "Claire Redfield", "affiliation": ["Civilian"], "debut": "Resident Evil 2, 1998"}
]

def index(req):
    return [c for c in chars], 200

def create(req):
    new_char = req.get_json()
    new_char["id"] = sorted([c["id"] for c in chars])[-1] + 1
    chars.append(new_char)
    return new_char, 201

def find_by_id(cid):
    try:
        char = [c for c in chars if c["id"] == cid]
        if len(char) == 0:
            return f"No agent with ID:{cid} found in Umbrella database"
        return char[0]
    except: 
        raise BadRequest(f"No agent with ID:{cid} found in Umbrella database")

def show(req, cid):
    return find_by_id(cid), 200

def update(req, cid):
    char = find_by_id(cid)
    data = req.get_json()
    for key, val in data.items():
        char[key] = val
    return char, 200

def destroy(req, cid):
    char = find_by_id(cid)
    chars.remove(char)
    return f"Agent {cid} has been terminated", 204