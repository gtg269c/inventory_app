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
        # AND user_name={user_name}"
        # AND user_name='{user_name}'"
        command = f"SELECT count(*) FROM user WHERE user_type='{user_type}' AND user_name='{user_name}'"
        result = self.execute_cmd(create_command=command)
        #list_row = []
        # for row in result:
        #    list_row.append(row)

        print(f"Return result: {result}")
        if result[0][0] == 1:
            return user_type
        else:
            return "no_match"


class ItemTable(Table):
    def __init__(self) -> None:
        super().__init__()

    def list_item(self):
        """ List all item in the table """
        command = f"SELECT * FROM item"
        return self.execute_cmd(create_command=command)

    def add_item(self, item_type: str,
                 item_name: str,
                 max_amount: int,
                 current_voume: int,
                 item_storage: int):
        """ Add items to the items table """
        command = f"INSERT INTO item VALUES('{item_type}', '{item_name}', '{max_amount}', '{current_voume}', '{item_storage}')"
        result = self.execute_cmd(create_command=command)

    def get_item(self, search_col: str, search_value: str):
        """ List items selected by the specific column """
        command = f"SELECT * FROM item WHERE {search_col}='{search_value}'"
        return self.execute_cmd(create_command=command)


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
