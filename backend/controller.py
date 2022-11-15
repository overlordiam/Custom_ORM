from utils import *
from flask import Flask, jsonify, request
import json
import os
from flask_cors import CORS, cross_origin
from app import Products, Controller, Users, Orders
from utils import getDataFromAPI

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

count = 0


@app.route("/product", methods=['POST'])
@cross_origin()
def WebsiteData():
    Controller.connectToDB(database_name="APP.db")
    PutProductsInDatabase(getDataFromAPI("https://dummyjson.com/", "products"))
    products = Products.objects.select("id, title, description, price, brand, category, thumbnail")
    print(products)
    return jsonify(products)

@app.route("/emptyCart", methods=["POST"])
@cross_origin()
def emptyCart():
    Controller.connectToDB(database_name="APP.db")
    Orders.objects.delete()
    return "Done"

@app.route("/products", methods=["POST"])
@cross_origin()
def getProducts():
    return jsonify(getDataFromAPI("https://dummyjson.com/","products"))

@app.route("/signUp", methods=["POST"])
@cross_origin()
def SignUp():
    Controller.connectToDB(database_name="APP.db")
    userId = request.json["userId"]
    email = request.json["email"]
    firstName = request.json["firstName"]
    lastName = request.json["lastName"]
    age = request.json["age"]
    gender = request.json["gender"]
    obj = [{"id": f"{userId}", "firstName": f"{firstName}", "lastName": f"{lastName}", "gender": f"{gender}", "age": f"{age}", "email": f"{email}"}]
    Users.objects.insert(obj)
    return "done"

@app.route("/updateProfile", methods=["POST"])
@cross_origin()
def Update():
    Controller.connectToDB(database_name="APP.db")
    # userId = request.json["userId"]
    firstName = request.json["firstName"]
    lastName = request.json["lastName"]
    age = request.json["age"]
    gender = request.json["gender"]
    obj = {"firstName": firstName, "lastName": lastName, "gender": gender, "age": age}
    Users.objects.update(data=obj)
    return "done"

@app.route("/delete", methods=["POST"])
@cross_origin()
def Delete():
    Controller.connectToDB(database_name="APP.db")
    # userId = request.json["userId"]
    Users.objects.delete()
    return "done"


@app.route("/addOrders", methods=["POST"])
@cross_origin()
def addOrders():
    Controller.connectToDB(database_name="APP.db")
    productId = request.json["id"]
    userId = request.json["userId"]
    quantity = request.json["quantity"]
    total = request.json["total"]
 
    obj = [{"id":"101", "userId": f"{userId}", "productId": f"{productId}", "quantity": f"{quantity}", "total":f"{total}"}]
   
    Orders.objects.insert(obj)

    return "done"

if __name__ == "__main__":
    Controller.connectToDB(database_name="APP.db")
    app.run(host='0.0.0.0', port=5000, debug=True)
