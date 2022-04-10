from flask import Flask, request, jsonify, make_response
import json

app = Flask(__name__)
@app.route("/login", methods=["POST"])
def json_example():
    req = request.get_json()
    if "username" not in req or "password" not in req:
        return make_response(jsonify({
            "message": "Invalid request"
        }), 400)

    with open('UsernamePassword.json') as logindetails:
        data = json.load(logindetails)

    username = req["username"]
    if username in data:
        if data[req["username"]] == req["password"]:
            return make_response(jsonify({
                "message": "Login successfull!",
                "sender": req["username"]
            }), 200)
        else:
            return make_response(jsonify({
                "message": "Invalid Username or password"
            }), 400)
    else:
        return make_response(jsonify({
            "message": "Invalid Username "
        }), 400)
   