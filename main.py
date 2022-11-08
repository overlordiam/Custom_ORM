from utils import getDataFromAPI, PutProductsInDatabase, PutOrdersInDatabase, PutUsersInDatabase, getProducts
from app import Products, Controller, Users, Orders

if __name__ == '__main__':
    Controller.connectToDB(database_name="APP.db")

    # PutProductsInDatabase(getDataFromAPI("https://dummyjson.com/", "products"))
    # getProducts()
    # products = Products.objects.select("id", "title")
    # print(products)
    # PutUsersInDatabase(getDataFromAPI("https://dummyjson.com/", "users"))
    # PutOrdersInDatabase(getDataFromAPI("https://dummyjson.com/", "carts"))
    Orders.objects.delete()
    Orders.objects.insert(getDataFromAPI("https://dummyjson.com/", "carts"))
    # Orders.objects.update(data={
    #     "id": 1, "userId": 1
    # })
    orders = Orders.objects.select("id", "userId", "productId")
    print(orders)

