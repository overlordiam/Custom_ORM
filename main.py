from utils import getDataFromAPI, PutProductsInDatabase, PutOrdersInDatabase, PutUsersInDatabase, getProducts, getUsers
from app import Products, Controller, Users, Orders
from flask import jsonify

if __name__ == '__main__':
    Controller.connectToDB(database_name="APP2.db")

    # PutProductsInDatabase(getDataFromAPI("https://dummyjson.com/", "products"))
    # getProducts()
    # products = Products.objects.select("id", "title")
    # print(products)
    # PutUsersInDatabase(getDataFromAPI("https://dummyjson.com/", "users"))
    # Users.objects.insert(getDataFromAPI("https://dummyjson.com/", "users"))
    # Users.objects.delete()
    # Users.objects.insert([{"id":"111","firstName":"suhaas","lastName":"gum","age":"20","gender":"male","email":"fnefnejf"}])
    users = Users.objects.select("id", "firstName", "age")
    print(users)
    # getUsers()
    # PutOrdersInDatabase(getDataFromAPI("https://dummyjson.com/", "carts"))
    # print(users)
    # Orders.objects.delete()
    # Orders.objects.insert([{'id': '100', 'userId': '100', 'productId': '100'}])
    # Orders.objects.update(data={
    #     "id": 1, "userId": 1
    # })
    # orders = Orders.objects.select("id", "userId", "productId")
    # print(orders)
    # PutProductsInDatabase(getDataFromAPI("https://dummyjson.com/", "products"))
    # print(getDataFromAPI("https://dummyjson.com/", "products")[0])
    # products = Products.objects.select("id", "title", "description")
    # print(products)
    # app.run(host='0.0.0.0', port=port)
    

