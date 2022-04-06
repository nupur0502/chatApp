from flask import Flask, request

app = Flask(__name__)
@app.route("/json", methods=["POST"])
def json_example():

    req = request.get_json()
    print(req)
    return req["idiot"]