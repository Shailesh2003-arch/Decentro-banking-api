from flask import Blueprint, jsonify, request
from bson import ObjectId
from db import transaction_collection, accounts_collection
from datetime import datetime



transaction_routes = Blueprint("transactions",__name__,url_prefix="/transactions")

@transaction_routes.post("/deposit")
def deposit():
    data = request.json
    accId = data["accountId"]
    amt = data["amount"]

    acc = accounts_collection.find_one({"_id":ObjectId(accId)})
    if not acc:
        return {"error":"Account not found"}, 404
    
    new_balance = acc["balance"] + amt

    accounts_collection.update_one({"_id":ObjectId(accId)},{"$set":{
        "balance":new_balance
    }})

    transaction = {
        "accountId":accId,
        "type":"deposit",
        "amount":amt,
        "createdAt":datetime.utcnow()
    }

    transaction_collection.insert_one(transaction)

    return {"newBalance":new_balance}


@transaction_routes.post("/withdrawl")
def withdraw():
    data = request.json
    accId = data["accountId"]
    amt = data["amount"]

    acc = accounts_collection.find_one({"_id":ObjectId(accId)})
    if not acc:
        return{
            "error":"Account not found"
        }, 404
    if acc["balance"] < amt:
        return {
            "error":"Insufficient funds"
        }, 400
    
    new_balance = acc["balance"] - amt

    accounts_collection.update_one({
        "_id": ObjectId(accId)
    },{
        "$set":{
            "balance": new_balance
        }
    })

    transaction = {
        "accountId":accId,
        "type":"withdraw",
        "amount":amt,
        "createdAt":datetime.utcnow()
    }

    transaction_collection.insert_one(transaction)

    return {
        "newBalance":new_balance
    }


@transaction_routes.post("/transfer")
def transfer():
    data = request.json
    fromAcc = data["from"]
    toAcc = data["to"]
    amount = data["amount"]


    sender = accounts_collection.find_one({"_id":ObjectId(fromAcc)})
    print(f"Sender is: {sender}")
    receiver = accounts_collection.find_one({"_id":ObjectId(toAcc)})
    print(f"Receiver is: {receiver}")

    
    if not sender or not receiver:
        return{
            "error":"One of the accounts not found"
        }, 404
    

    if sender["balance"] < amount:
        return{
            "error":"Insufficient funds"
        }, 400
    
    accounts_collection.update_one({
    "_id":ObjectId(fromAcc)},
    {"$inc":{
        "balance": -amount
    }}
    )


    accounts_collection.update_one({
        "_id":ObjectId(toAcc)
    },{
        "$inc":{
            "balance": amount
        }
    })



    transaction_collection.insert_many([
        {
            "accountId":fromAcc,
            "type":"transfer-out",
            "amount":amount,
            "to": toAcc,
            "createdAt":datetime.utcnow()
        },
        {
            "accountId":toAcc,
            "type":"transfer-in",
            "amount":amount,
            "from": fromAcc,
            "createdAt":datetime.utcnow() 
        }
    ])

    return{
        "message":"Transfer successful"
    }



@transaction_routes.get("/<account_id>")
def history(account_id):
    transactions = list( transaction_collection.find({"accountId":account_id}).sort("createdAt",-1))

    for trx in transactions:
        trx["_id"] = str(trx["_id"])

    return jsonify(transactions)