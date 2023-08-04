from utils import getDataFromAPI, PutProductsInDatabase, PutOrdersInDatabase, PutUsersInDatabase, getProducts, getUsers
from app import Products, Controller, Users, Orders
from flask import jsonify

if __name__ == '__main__':
    Controller.connectToDB(database_name="APP2.db")

    PutProductsInDatabase(getDataFromAPI("https://dummyjson.com/", "products"))
    # getProducts()
    # products = Products.objects.select("id", "title")
    # print(products)
    PutUsersInDatabase(getDataFromAPI("https://dummyjson.com/", "users"))
    # Users.objects.insert(getDataFromAPI("https://dummyjson.com/", "users"))
    # Users.objects.delete()
    users = Users.objects.select("id", "firstName", "age")
    print(users)
    # getUsers()
    # PutOrdersInDatabase(getDataFromAPI("https://dummyjson.com/", "carts"))
    # Orders.objects.delete()
    # print(orders)
    # app.run(host='0.0.0.0', port=port)
    

