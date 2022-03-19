"""the module contains users of the inventory management system
- User: parent
- NewUser: child
- Admiistrator: child
- Lab manager: child
- resercher: child
"""
from traceback import print_tb
from src.database import *


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

    def search_item(self):
        try:
            search_col = input('Enter search column: ')
            search_value = input('Enter search value: ')

        except:
            print(f'Invalid entry')

        i = ItemTable()
        results = i.get_item(search_col=search_col, search_value=search_value)
        print(f"item_type   item_name   max_amount  current_amount  item_storage")
        for result in results:
            print(
                f"{result[0]}   {result[1]}    {result[2]} {result[3]}  {result[4]}")


class NewUser(User):
    """Child class for new user. It porivides methods to 
    - create new users
    """

    def __init__(self) -> None:
        super().__init__()

    def create_user(self):
        """ Get input for user name """
        try:
            self.user_type = input('Enter user type (manager/scientist): ')
            self.user_name = input('Enter user name: ')
        except:
            print(f'Invalid entry')

    def add_user_db(self):
        """ Add new user to user database """
        a_user = UserTable()
        a_user.add_user(self.user_type, self.user_name)

    def __str__(self) -> str:
        return f"Type: {self.user_type}, Name: {self.user_name}"


class LabManager(User):
    """ Child class for lab manager. It allows the following task
    - get low inventory
    - search items in inventory
    - List items low in inventory
    """

    def __init__(self) -> None:
        super().__init__()
        self.continue_greeting = True
        self.menu()

    def menu(self):
        self.greeting_options = [
            (0, "Main menu"),
            (1, "Search item"),
            (2, "Get low inventory"),
            (3, "Add item to inventory")
        ]

        while self.continue_greeting:

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
                self.continue_greeting = False

    def get_low_inventory(self, cutoff: int = 30):
        i = ItemTable()
        results = i.list_item()

        print(f'***** Items wth low inventory ********')
        print(f"item_type   item_name   max_amount  current_amount  item_storage")
        for result in results:
            if (result[3]/result[2])*100 <= cutoff:
                print(
                    f"{result[0]}   {result[1]}    {result[2]} {result[3]}  {result[4]}")

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

    # def search_item(self):
    #    try:
    #        search_col = input('Enter search column: ')
    #        search_value = input('Enter search value: ')
#
    #    except:
    #        print(f'Invalid entry')
#
    #    i = ItemTable()
    #    results = i.get_item(search_col=search_col, search_value=search_value)
    #    print(f"item_type   item_name   max_amount  current_amount  item_storage")
    #    for result in results:
    #        print(
    #            f"{result[0]}   {result[1]}    {result[2]} {result[3]}  {result[4]}")


class Researcher(User):
    """ Child class for reseachers. It allows the following methods.
    - get item and update the invetory
    - search the inventory

    """

    def __init__(self) -> None:
        super().__init__()
        self.continue_greeting = True
        self.menu()

    def menu(self):
        """ Menu for the researcher portal """
        self.greeting_options = [
            (0, "Main menu"),
            (1, "Search item"),
            (2, "Get item"),
        ]

        while self.continue_greeting:

            print(f"Welcome to the **Scientist** portal.")
            print(f"What will you like to do? (choose an option)")
            for key, value in self.greeting_options:
                print(f"Press {key} to {value}")
            user_input = int(input("choose an option: "))

            if user_input == 1:
                self.search_item()
            elif user_input == 2:
                self.get_item()
            else:
                print(f"Exiting ** Scientist ** system.\n")
                self.continue_greeting = False

    def get_item(self):
        """ Get item from invetory and update the amount """
        try:
            item_name = input('Enter item name: ')
            item_amount = input('Enter item amount: ')

        except:
            print(f'Invalid entry')
        i = ItemTable()
        message = i.get_update_item(
            item_name=item_name, item_amount=int(item_amount))
        print(message)
