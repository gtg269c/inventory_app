"""the module contains users of the inventory management system
- User: parent
- NewUser: child
- Admiistrator: child
- Lab manager: child
- resercher: child
"""
from src.database import Table, UserTable, create_table


class User():
    """ The parent class provides common attributes
    and methods for different types of users.
    """

    def __init__(self, user_type, user_name) -> None:
        self.user_type = user_type
        self.user_name = user_name

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

    def __init__(self, user_type, user_name) -> None:
        super().__init__(user_type, user_name)
        # if not db.table.user:
        self.add_user_db()

    @classmethod
    def create_user(cls):
        while 1:
            try:
                user_type = input('Enter user type (manager/scientist): ')
                user_name = input('Enter user name: ')
                return(user_type, user_name)
            except:
                print(f'Invalid entry')
                continue

    def list_table(self):
        pass

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
