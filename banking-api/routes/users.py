from flask import Blueprint, request, jsonify
from db import users_collection
from bson import ObjectId

user_routes = Blueprint("users",__name__, url_prefix="/users")


@user_routes.post("/")
def create_user():
    data = request.json
    user={
        "name":data["name"],
        "email":data["email"]
    }
    res = users_collection.insert_one(user)
    user["_id"] = str(res.inserted_id)
    return jsonify(user),201
