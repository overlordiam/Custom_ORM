import requests
import json
import sqlite3


def getDataFromAPI(api, category):
    """
    Fetches data from the specified API for the given category.

    Args:
        api (str): The base URL of the API.
        category (str): The category of data to fetch (e.g., "products", "users", "carts").

    Returns:
        list: A list containing the data retrieved from the API in dictionary format.
    """
    response = requests.get(api + category)
    print(response.status_code)
    data = response.text
    json_data = json.loads(data)
    json_data = json_data[category]
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
                        dict_.update({
                            "productId": product["id"],
                            "quantity": product["quantity"],
                            "total": product["total"]
                        })
                        result.append(dict_.copy())
                    break
    return result


def PutProductsInDatabase(data):
    """
    Inserts product data into the 'products' table in the database.

    Args:
        data (list): A list of dictionaries containing product data to be inserted.

    Returns:
        None
    """
    con = sqlite3.connect("APP2.db")
    cur = con.cursor()
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
    """
    Inserts user data into the 'users' table in the database.

    Args:
        data (list): A list of dictionaries containing user data to be inserted.

    Returns:
        None
    """
    con = sqlite3.connect("APP2.db")
    cur = con.cursor()
    field_names = ["id", "firstName", "lastName", "age", "gender", "email"]
    res = cur.execute("SELECT name FROM sqlite_master WHERE name='users'")
    if res.fetchone() is None:
        cur.execute("CREATE TABLE users(id, firstName, lastName, age, gender, email)")
    for row in data:
        values = list()
        values += [row[field_name] for field_name in field_names]
        cur.execute("INSERT INTO users VALUES(?,?,?,?,?,?)", values)
    con.commit()


def PutOrdersInDatabase(data):
    """
    Inserts order data into the 'orders' table in the database.

    Args:
        data (list): A list of dictionaries containing order data to be inserted.

    Returns:
        None
    """
    con = sqlite3.connect("APP2.db")
    cur = con.cursor()
    field_names = ["id", "userId", "productId", "quantity", "total"]
    res = cur.execute("SELECT name FROM sqlite_master WHERE name='orders'")
    if res.fetchone() is None:
        cur.execute("CREATE TABLE orders(id int auto_increment primary key, userId, productId, quantity, total)")
    for row in data:
        values = list()
        values += [row[field_name] for field_name in field_names]
        cur.execute("INSERT INTO orders VALUES(?,?,?,?,?)", values)
    con.commit()


def getProducts():
    """
    Fetches and prints product data from the 'products' table in the database.

    Returns:
        None
    """
    con = sqlite3.connect("APP2.db")
    cur = con.cursor()
    for row in cur.execute("SELECT * FROM products"):
        print(row)


def getUsers():
    """
    Fetches and prints user data from the 'users' table in the database.

    Returns:
        None
    """
    con = sqlite3.connect("APP2.db")
    cur = con.cursor()
    for row in cur.execute("SELECT * FROM users"):
        print(row)
