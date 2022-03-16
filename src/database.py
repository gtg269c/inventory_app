"""module to interact with the database
"""

import sqlite3


class Table():
    def __init__(self) -> None:
        self.connection = sqlite3.connect('inventory.db')

    def execute_cmd(self, create_command: str):
        cursor = self.connection.cursor()

        cursor.execute(create_command)
        result = cursor.fetchall()

        self.connection.commit()
        self.connection.close()
        return result


class UserTable(Table):

    def __init__(self) -> None:
        super().__init__()

    def add_user(self, user_type: str, user_name: str):
        command = f"INSERT INTO user VALUES('{user_type}','{user_name}')"
        self.execute_cmd(create_command=command)

    def authenticate_user(self,  user_type: str, user_name: str):
        command = f"SELECT count(*) FROM user WHERE user_type={user_type} AND user_name={user_name}"
        user_type = ''
        result = self.execute_cmd(create_command=command)
        if result == 1:
            return user_type
        else:
            return "no_match"


class ItemTable(Table):
    def __init__(self) -> None:
        super().__init__()

    def search_item(self):
        pass

    def list_item(self):
        pass

    def add_item(self):
        pass

    def get_item(self):
        pass


class NewTable(Table):

    createtb_user = """create table if not exists user(
                user_type text,
                user_name text
            )
            """

    createtb_item = """create table if not exists item(
                item_type text,
                item_name text,
                max_amount integer,
                current_volume integer,
                item_storage integer
            )
            """

    list_table = "SELECT name FROM sqlite_master WHERE type='table';"

    def create_table(self, command: str):

        connection = sqlite3.connect('inventory.db')
        cursor = connection.cursor()
        cursor.execute(command)
        connection.commit()
        connection.close()
