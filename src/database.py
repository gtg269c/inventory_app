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
    """class to interact with the user table 

    Args:
        Table (class): parent class
    """

    def __init__(self) -> None:
        super().__init__()

    def add_user(self, user_type: str, user_name: str):
        """ Adds user to the table """
        command = f"INSERT INTO user VALUES('{user_type}','{user_name}')"
        self.execute_cmd(create_command=command)

    def authenticate_user(self,  user_type: str, user_name: str):
        """ Authenticates the user login """
        command = f"SELECT count(*) FROM user WHERE user_type='{user_type}' AND user_name='{user_name}'"
        result = self.execute_cmd(create_command=command)

        print(f"Return result: {result}")
        if result[0][0] == 1:
            return user_type
        else:
            return "no_match"


class ItemTable(Table):
    """class to interact with the items table 

    Args:
        Table (class): parent class
    """

    def __init__(self) -> None:
        super().__init__()

    def list_item(self):
        """ List all item in the table """
        command = f"SELECT * FROM item"
        return self.execute_cmd(create_command=command)

    def add_item(self, item_type: str,
                 item_name: str,
                 max_amount: int,
                 current_volume: int,
                 item_storage: int):
        """ Add items to the items table """
        command = f"INSERT INTO item VALUES('{item_type}', '{item_name}', '{max_amount}', '{current_volume}', '{item_storage}')"
        result = self.execute_cmd(create_command=command)

    def get_item(self, search_col: str, search_value: str):
        """ List items selected by the specific column """
        command = f"SELECT * FROM item WHERE {search_col}='{search_value}'"
        return self.execute_cmd(create_command=command)

    def get_current_amount(self, item_name: str):
        command_amount = f"SELECT current_volume FROM item WHERE item_name='{item_name}'"
        return self.execute_cmd(create_command=command_amount)

    def get_update_item(self, item_name: str, item_amount: int):
        """ Get item from the inventory and update the inventory """
        result_amount = self.get_current_amount(item_name=item_name)
        current_amount = result_amount[0][0]

        if current_amount > item_amount:
            new_amount = current_amount - item_amount
            command = f"UPDATE item SET current_volume='{new_amount}' WHERE item_name='{item_name}';"
            t = Table()
            t.execute_cmd(create_command=command)
            return f"Sucessfully got {item_name} and updated amount to {new_amount}"
        else:
            return f"Sorry, current amount of {item_name} is insufficient."


class NewTable(Table):
    """class to create new tables

    Args:
        Table (parent class): parent class
    """

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
        """ method to execute sql command with sqlite """

        connection = sqlite3.connect('inventory.db')
        cursor = connection.cursor()
        cursor.execute(command)
        connection.commit()
        connection.close()
