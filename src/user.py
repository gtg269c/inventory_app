"""the module contains users of the inventory management system
- User: parent
- NewUser: child
- Admiistrator: child
- Lab manager: child
- resercher: child
"""
from src.database import *


class User():
    """ The parent class provides common attributes
    and methods for different types of users.
    """

    def __init__(self) -> None:
        pass

    def list_table(self):
        pass

    def add_user_db(self):
        user = UserTable()
        user.add_user(self.user_type, self.user_name)


class NewUser(User):
    createdb_command = """"CREATE TABLE IF NOT EXISTS user(
            user_type text,
            user_name text
        )
        """

    def __init__(self) -> None:
        super().__init__()

    def create_user(self):
        try:
            self.user_type = input('Enter user type (manager/scientist): ')
            self.user_name = input('Enter user name: ')
        except:
            print(f'Invalid entry')

    def add_user_db(self):
        user = UserTable()
        user.add_user(self.user_type, self.user_name)

    def __str__(self) -> str:
        return f"Type: {self.user_type}, Name: {self.user_name}"


class LabManager(User):
    def get_low_inventory(self, cutoff: int = 30):
        pass

    def add_item(self):
        pass

    def get_item(self):
        pass

    def search_item(self):
        pass


class Researcher(User):
    def search_item(self):
        pass

    def get_item(self):
        pass
