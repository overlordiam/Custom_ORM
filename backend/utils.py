import requests
import json
import sqlite3


def getDataFromAPI(api, category):
    response = requests.get(api + category)
    print(response.status_code)
    data = response.text
    json_data = json.loads(data)
    json_data = json_data[category]
    # print(json_data)
    result = []
    if category == "products":
        for data in json_data:
            result.append({key: value for key, value in data.items() if
                           key not in ["rating", "discountPercentage", "stock", "images"]})
    elif category == "users":
        for data in json_data:
            result.append({key: value for key, value in data.items() if
                           key in ["id", "firstName", "lastName", "age", "gender", "email"]})
    elif category == "carts":
        for data in json_data:
            dict_ = dict()
            dict_.update({key: value for key, value in data.items() if
                          key in ["id", "userId"]})
            for key, value in data.items():
                if key == "products":
                    for product in data[key]:
                        # print(product)
                        dict_.update({
                            "productId": product["id"],
                            "quantity": product["quantity"],
                            "total": product["total"]
                        })
                        # print(dict_)
                        result.append(dict_.copy())
                        # print(result)

                    break
    # print(result)
    return result


def PutProductsInDatabase(data):
    con = sqlite3.connect("APP.db")
    cur = con.cursor()
    cur.execute("DROP TABLE products")
    res = cur.execute("SELECT name FROM sqlite_master WHERE name='products'")
    if res.fetchone() is None:
        cur.execute("CREATE TABLE products(id,title,description,price,brand,"
                    "category,thumbnail)")
    field_names = ["id", "title", "description", "price", "brand", "category", "thumbnail"]
    for row in data:
        values = list()
        values += [row[field_name] for field_name in field_names]
        cur.execute("INSERT INTO products VALUES(?,?,?,?,?,?,?)", values)
    con.commit()


def PutUsersInDatabase(data):
    con = sqlite3.connect("APP.db")
    cur = con.cursor()
    field_names = ["id", "firstName", "lastName", "age", "gender", "email"]
    # cur.execute("DROP TABLE users")
    res = cur.execute("SELECT name FROM sqlite_master WHERE name='users'")
    if res.fetchone() is None:
        cur.execute("CREATE TABLE users(id, firstName, lastName, age, gender, email)")
    for row in data:
        values = list()
        values += [row[field_name] for field_name in field_names]
        cur.execute("INSERT INTO users VALUES(?,?,?,?,?,?)", values)
    con.commit()


def PutOrdersInDatabase(data):
    con = sqlite3.connect("APP.db")
    cur = con.cursor()
    cur.execute("DROP TABLE orders")
    field_names = ["id", "userId", "productId", "quantity", "total"]
    res = cur.execute("SELECT name FROM sqlite_master WHERE name='orders'")
    if res.fetchone() is None:
        cur.execute("CREATE TABLE orders(id, userId, productId, quantity, total)")
    for row in data:
        values = list()
        values += [row[field_name] for field_name in field_names]
        cur.execute("INSERT INTO orders VALUES(?,?,?,?,?)", values)
    con.commit()


def getProducts():
    con = sqlite3.connect("APP.db")
    cur = con.cursor()
    for row in cur.execute("SELECT * FROM products"):
        print(row)
