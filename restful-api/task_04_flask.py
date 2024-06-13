from flask import Flask
from flask import jsonify
from flask import request
import json
app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


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
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.json
    if data is None:
        return jsonify({"error": "Data not provided"}), 400
    if 'username' not in data or not data['username']:
        return jsonify({"error": "Username is required"}), 400
    username = data['username']
    diction = {
        'username': username,
        'name': data.get('name'),
        'age': data.get('age'),
        'city': data.get('city')
    }
    users[username] = diction
    return jsonify({"message": "User added", "user": diction}), 201


if __name__ == "__main__":
    app.run()
