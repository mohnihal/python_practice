import sqlite3

class SQliteSetUp:
    DB_NAME = 'new_db.db3'
    TABLE_NAME = 'employee'
    db = None
    cursor = None

    def setup_connection(cls):
        cls.db = sqlite3.connect(cls.DB_NAME)
        cls.cursor = cls.db.cursor()


class InsertQueries:
    sample_table = 'employee'
    sample_values = ['Roger', 'Moore', 'Accounts', 52000]
    template = f"INSERT INTO {sample_table} (FirstName, LastName, Department, Salary) VALUES ('{sample_values[0]}', '{sample_values[1]}', '{sample_values[2]}', '{sample_values[3]}');"
    db = None
    cursor = None


    def _decorator(func):
        def magic(cls):
            if cls.db == None:
                cls.db = sqlite3.connect('sql_practice/new_db.db3')
                cls.cursor = cls.db.cursor()
            func(cls)
            if func.__name__ == 'execute_query':
                cls.db.commit()
            cls.cursor.close()
            cls.db.close()
        return magic

    @classmethod
    def print_query(cls):
        print(cls.template)
    
    @classmethod
    @_decorator
    def execute_query(cls):
        return cls.cursor.execute(cls.template)


InsertQueries.execute_query()