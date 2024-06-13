from flask import Flask
from flask import requests
from flask import jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "menimgizlikeyim"
jwt = JWTManager(app)


users = {
     "user1": {"username": "user1", "password": generate_password_hash("tahir12345"), "role": "user"},
     "admin1": {"username": "admin1", "password": generate_password_hash("tahir54321"), "role": "admin"}
}




@app.route("/basic-protected", methods="[GET]")
@auth.login_required
def basicprotected():
    return "Basic Auth: Access Granted"

@app.route("/login", methods="[POST]")
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username in users and check_password_hash(users.get(username)['password'], password):
        access_token = create_access_token(identity=username)
        return jsonify(username)
    return "Unauthorized", 401

@app.route('/jwt-protected', methods="[GET]")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200

@app.route('/admin-only', methods="[GET]")
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return jsonify("Admin Access: Granted"), 200





@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
