from utils import getDataFromAPI, PutProductsInDatabase, PutOrdersInDatabase, PutUsersInDatabase, getProducts, getUsers
from app import Products, Controller, Users, Orders
from flask import jsonify

if __name__ == '__main__':
    Controller.connectToDB(database_name="APP.db")

    # PutProductsInDatabase(getDataFromAPI("https://dummyjson.com/", "products"))
    # products = Products.objects.select("id", "title")
    # print(products)
    # PutUsersInDatabase(getDataFromAPI("https://dummyjson.com/", "users"))
    # Users.objects.insert(getDataFromAPI("https://dummyjson.com/", "users"))
    # Users.objects.delete()
    users = Users.objects.select("id", "firstName", "age")
    print(users)


    # PutOrdersInDatabase(getDataFromAPI("https://dummyjson.com/", "carts"))
    # print(users)
    # Orders.objects.delete()
    # Orders.objects.insert([{'id': '100', 'userId': '100', 'productId': '100'}])
    # Orders.objects.update(data={
    #     "id": 1, "userId": 1
    # })
    # orders = Orders.objects.select("id", "userId", "productId", "quantity", "total")
    # print(orders)
    

