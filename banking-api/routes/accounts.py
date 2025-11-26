from flask import request, Blueprint, jsonify
from db import accounts_collection
from bson import ObjectId


account_routes = Blueprint("accounts",__name__,url_prefix="/accounts")

@account_routes.post("/")
def create_account():
    data = request.json
    account = {
        "userId":data["userId"],
        "balance":0
    }
    res = accounts_collection.insert_one(account)
    account["_id"] = str(res.inserted_id)
    return jsonify(account), 201


@account_routes.get("/<account_id>/balance")
def get_balance(account_id):
    acc = accounts_collection.find_one({"_id":ObjectId(account_id)})
    if not acc:
        return{
            "error":"Account not found"
        },404
    
    return {"balance":acc["balance"]}

