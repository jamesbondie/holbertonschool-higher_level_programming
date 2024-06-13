from flask import Flask
from flask import jsonify
from flask import request
import json
app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API"


@app.route("/data")
def data():
    x = []
    for i in users.keys():
        x.append(i)
    return jsonify(x)


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def user(username):
    for i in users.keys():
        if i == username:
            return jsonify(users[i])
    else:
        return jsonify({"error": "User not found"})


@app.route("/add_user", methods=['GET', 'POST'])
def add_user():
    data = request.json
    diction = {}
    diction.update({data['username']: data})
    users.update(diction)
    return jsonify({"message": "User added"}, diction)


if __name__ == "__main__":
    app.run()
