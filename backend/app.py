import sqlite3
import json

class Controller:
    con = None

    @classmethod
    def connectToDB(cls, database_name):
        con = sqlite3.connect(database_name)
        cls.con = con

    @classmethod
    def _get_cursor(cls):
        return cls.con.cursor()

    @classmethod
    def _execute_query(cls, query, params=None):
        cursor = cls._get_cursor()
        if params is None:
            cursor.execute(query)
        else:
            cursor.execute(query, params)

    @classmethod
    def _execute_many_query(cls, query, params=None):
        cursor = cls._get_cursor()
        cursor.executemany(query, params)

    def __init__(self, model_class):
        self.model_class = model_class

    def select(self, *fields):
        """
        Implements the select equivalent of SQL
        """
        fields_format = ",".join(fields)
        query = f"SELECT {fields_format} FROM {self.model_class.table_name}"
        cursor = self._get_cursor()
        cursor.execute(query)

        model_objects = []
        # result = cursor.fetchmany(size=30)
        for row_values in cursor.execute(query):
            # print(fields, row_values)
            keys, values = fields, row_values
            row_data = dict(zip(keys, values))
            # print(row_data)
            model_objects.append(self.model_class(**row_data))
            # print(model_objects)
        cursor.close()

        return model_objects

    def insert(self, rows):
        field_names = rows[0].keys()
        assert all(row.keys() == field_names for row in rows[1:])
        cursor = self._get_cursor()


        field_format = ", ".join(field_names)
        value_format = ", ".join([f'({", ".join("?" * len(field_names))})'])

        query = f"INSERT INTO {self.model_class.table_name} ({field_format}) VALUES {value_format}"

        for row in rows:
            row_values = [row[field_name] for field_name in field_names]
            cursor.execute(query, row_values)

        self.con.commit()
        cursor.close()
        return "none"


    def update(self, data: dict):
        field_names = data.keys()
        placeholder = ", ".join([f"{field_name}=?" for field_name in field_names])
        query = f"UPDATE {self.model_class.table_name} SET {placeholder}"

        params = tuple(data.values())
        cursor = self._get_cursor()

        cursor.execute(query, params)

        self.con.commit()
        cursor.close()

        return "none"


    def delete(self, id=None):

        cursor = self._get_cursor()

        if id is not None:
             query = f"DELETE FROM {self.model_class.table_name} WHERE id=?"
             cursor.execute(query, id)

        else:
            query = f"DELETE FROM {self.model_class.table_name}"
            cursor.execute(query)

        self.con.commit()
        cursor.close()

        return "none"


class MetaModel(type):

    def _get_manager(cls):
        return cls.controller_class(model_class=cls)

    @property
    def objects(cls):
        return cls._get_manager()


class Display(metaclass=MetaModel):
    """
    This class is to display the values after a query execution.
    Any other class can inherit this class and display its results.
    """
    table_name = ""

    def __init__(self, **row_data):
        for field_name, value in row_data.items():
            setattr(self, field_name, value)

    def __repr__(self):
        """
        Prints out the results of the query executions in command line
        """
        # attrs_format = {{f"{field}":f"{value}" for field, value in self.__dict__.items()}}
        # return attrs_format
        # return f"{self.__class__.__name__}: ({attrs_format})\n"
        dic = dict()
        for keys, values in self.__dict__.items():
            dic.update({f"{keys}":f"{values}"})
        return f"({dic})"


class Products(Display):
    controller_class = Controller
    table_name = "products"


class Users(Display):
    controller_class = Controller
    table_name = "users"


class Orders(Display):
    controller_class = Controller
    table_name = "orders"
