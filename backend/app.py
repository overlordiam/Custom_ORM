import sqlite3
import json

class Controller:
    con = None

    @classmethod
    def connectToDB(cls, database_name):
        """
        Connects to the SQLite database with the given name.

        Parameters:
            database_name (str): The name of the SQLite database.

        Returns:
            None
        """
        con = sqlite3.connect(database_name)
        cls.con = con

    @classmethod
    def _get_cursor(cls):
        """
        Returns the cursor object associated with the database connection.

        Returns:
            sqlite3.Cursor: The cursor object.
        """
        return cls.con.cursor()

    @classmethod
    def _execute_query(cls, query, params=None):
        """
        Executes the given SQL query with optional parameters.

        Parameters:
            query (str): The SQL query to be executed.
            params (tuple, optional): The parameters to be substituted in the query.

        Returns:
            None
        """
        cursor = cls._get_cursor()
        if params is None:
            cursor.execute(query)
        else:
            cursor.execute(query, params)

    @classmethod
    def _execute_many_query(cls, query, params=None):
        """
        Executes the given SQL query multiple times with different sets of parameters.

        Parameters:
            query (str): The SQL query to be executed multiple times.
            params (list of tuples, optional): The list of parameter sets for each execution.

        Returns:
            None
        """
        cursor = cls._get_cursor()
        cursor.executemany(query, params)

    def __init__(self, model_class):
        """
        Initializes the Controller with the associated model class.

        Parameters:
            model_class (type): The class of the model to be controlled.

        Returns:
            None
        """
        self.model_class = model_class

    def select(self, *fields):
        """
        Performs a SELECT query on the database for the given fields.

        Parameters:
            *fields (str): The fields to be selected in the query.

        Returns:
            list: A list of model objects representing the results of the query.
        """
        fields_format = ",".join(fields)
        query = f"SELECT {fields_format} FROM {self.model_class.table_name}"
        cursor = self._get_cursor()
        cursor.execute(query)

        model_objects = []
        for row_values in cursor.execute(query):
            keys, values = fields, row_values
            row_data = dict(zip(keys, values))
            model_objects.append(self.model_class(**row_data))
        return model_objects

    def insert(self, rows):
        """
        Inserts rows into the database.

        Parameters:
            rows (list of dict): A list of dictionaries representing the rows to be inserted.

        Returns:
            None
        """
        field_names = rows[0].keys()
        assert all(row.keys() == field_names for row in rows[1:])

        field_format = ", ".join(field_names)
        value_format = ", ".join([f'({", ".join("?" * len(field_names))})'])

        query = f"INSERT INTO {self.model_class.table_name} ({field_format}) VALUES {value_format}"

        for row in rows:
            row_values = [row[field_name] for field_name in field_names]
            self._execute_query(query, row_values)
        
        self.con.commit()

    def update(self, data):
        """
        Updates rows in the database with the given data.

        Parameters:
            data (dict): A dictionary representing the fields and their updated values.

        Returns:
            None
        """
        field_names = data.keys()
        placeholder = ", ".join([f"{field_name}=?" for field_name in field_names])
        query = f"UPDATE {self.model_class.table_name} SET {placeholder}"

        params = tuple(data.values())
        self._execute_query(query, params)

        self.con.commit()

    def delete(self):
        """
        Deletes all rows from the database table.

        Returns:
            None
        """
        query = f"DELETE FROM {self.model_class.table_name}"
        self._execute_query(query)

        self.con.commit()


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
        """
        Initializes the Display object with the given row data.

        Parameters:
            **row_data (dict): The row data for the object.

        Returns:
            None
        """
        for field_name, value in row_data.items():
            setattr(self, field_name, value)

    def __repr__(self):
        """
        Returns the string representation of the Display object.

        Returns:
            str: The string representation.
        """
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
