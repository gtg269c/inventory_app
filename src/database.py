"""module to interact with the database
"""

import sqlite3


# connection == sqlite3.connect('customer.db')


def get_tables():
    pass


createtb_user = """create table user(
            user_type text,
            user_name text
        )
        """

createtb_item = """create table item(
            user_type text,
            user_name text
        )
        """


def create_table(command: str):
    connection = sqlite3.connect('inventory.db')
    cursor = connection.cursor()
    cursor.execute(createtb_user)
    connection.commit()
    connection.close()


class Table():
    def __init__(self) -> None:
        self.connection = sqlite3.connect('inventory.db')

    def execute_cmd(self, create_command: str):
        cursor = self.connection.cursor()

        cursor.execute(create_command)

        self.connection.commit()
        self.connection.close()
        return cursor.fetchall()

    def list_tables(self):
        return self.execute_cmd("SELECT name FROM sqlite_master WHERE type='table';")

    def add_record(self):
        pass

    def update_record(self):
        pass

    def delete_record(self):
        pass


class UserTable(Table):

    def __init__(self) -> None:
        super().__init__()

    def add_user(self, user_type: str, user_name: str):
        command = f"INSERT INTO user VALUES('{user_type}','{user_name}')"
        self.execute_cmd(create_command=command)
