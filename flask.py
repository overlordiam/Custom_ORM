from flask import Flask, jsonify
import os
from flask_cors import CORS, cross_origin
from app import Products, Controller, Users, Orders

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['POST'])
@cross_origin()
def WebsiteData():
    products = Products.objects.select("id, title, description, price, brand, category, thumbnail")
    return jsonify(products)

@app.route("/signUp", methods=["POST"])
@cross_origin()
def SignUp():
    pass


if __name__ == "__main__":
    Controller.connectToDB(database_name="APP.db")
    app.run(host='0.0.0.0', port=8000, debug=True)
