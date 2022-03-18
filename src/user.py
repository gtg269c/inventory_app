"""the module contains users of the inventory management system
- User: parent
- NewUser: child
- Admiistrator: child
- Lab manager: child
- resercher: child
"""
from src.database import *
import sys


class User():
    """ The parent class provides common attributes
    and methods for different types of users.
    """

    def __init__(self) -> None:
        pass

    def menu(self):
        pass

    def list_table(self):
        pass

    def add_user_db(self):
        pass


class NewUser(User):

    def __init__(self) -> None:
        super().__init__()

    def create_user(self):
        try:
            self.user_type = input('Enter user type (manager/scientist): ')
            self.user_name = input('Enter user name: ')
        except:
            print(f'Invalid entry')

    def add_user_db(self):
        a_user = UserTable()
        a_user.add_user(self.user_type, self.user_name)

    def verify_user(self):
        v_user = UserTable()
        if v_user.authenticate_user:
            if self.user_type == 'manager':
                LabManager().menu()
            elif self.user_type == 'scientist':
                Researcher()
        else:
            print(f"Unvalid user, Access denied")
            sys.exit()

    def __str__(self) -> str:
        return f"Type: {self.user_type}, Name: {self.user_name}"


class LabManager(User):

    def __init__(self) -> None:
        super().__init__()
        self.greeting_options = [
            (0, "Main menu"),
            (1, "Search item"),
            (2, "Get low inventory"),
            (3, "Add item to inventory")
        ]

    def menu(self):
        print(f"Welcome to the **Managers** portal.")
        print(f"What will you like to do? (choose an option)")
        for key, value in self.greeting_options:
            print(f"Press {key} to {value}")
        user_input = int(input("choose an option: "))

        if user_input == 3:
            self.add_item()
        elif user_input == 1:
            self.search_item()
        elif user_input == 2:
            self.get_low_inventory()
        else:
            print(f"Exiting ** Managers ** system.\n")

    def get_low_inventory(self, cutoff: int = 30):
        pass

    def add_item(self):
        try:
            item_type = input('Enter item type: ')
            item_name = input('Enter item name: ')
            max_amount = input('Enter max amount: ')
            current_volume = input('Enter current volume: ')
            item_storage = input('Enter item type: ')

        except:
            print(f'Invalid entry')
        i = ItemTable()
        i.add_item(item_type=item_type, item_name=item_name, max_amount=max_amount,
                   current_voume=current_volume, item_storage=item_storage)

    def search_item(self):
        pass


class Researcher(User):
    def menu(self):
        print(f"Welcome to the lab inventory system.")
        print(f"What will you like to do? (choose an option)")
        for key, value in greeting_options:
            print(f"Press {key} to {value}")
        user_input = int(input("choose an option: "))

    def search_item(self):
        pass

    def get_item(self):
        pass
