from utils import *
from controller import Controller, Users, Products, Orders
import pytest

def select():
    Controller.connectToDB(database_name="APP.db")
    users = Users.objects.select("id, firstName, lastName")
    return users 

def insert():
    Controller.connectToDB(database_name="APP.db")
    Users.objects.insert([{"id": "100", "firstName": "suhaas", "lastName": "gummalam", "gender": "male", "age": "22"}])
    return "ok"

def update():
    Controller.connectToDB(database_name="APP.db")
    obj = {"id": 100, "firstName": "suhaas", "lastName": "gummalam", "gender": "male", "age": 22}

    Users.objects.update(obj)
    return "ok"

def delete():
    Controller.connectToDB(database_name="APP.db")
    Users.objects.delete()
    return "ok"

def test_select():
    assert len(select()) > 0

def test_insert():
    assert insert() == "ok"

def test_update():
    assert update() == "ok"

def test_delete():
    delete()
    assert len(Users.objects.select("id")) == 0

