"""main page for the inventory app
"""

import os
from src.user import LabManager, User, NewUser
from src.database import UserTable, NewTable


class Inventory():
    def __init__(self) -> None:
        self.continue_greeting = True
        self.greeting()

    def greeting(self):

        greeting_options = [
            (0, "exit system"),
            (1, "login"),
            (2, "create database"),
            (3, "create user")
        ]

        while self.continue_greeting:

            print(f"Welcome to the lab inventory system.")
            print(f"What will you like to do? (choose an option)")
            for key, value in greeting_options:
                print(f"Press {key} to {value}")
            user_input = int(input("choose an option: "))

            if user_input == 3:
                self.create_user()

            elif user_input == 1:
                self.login_user()

            elif user_input == 2:
                self.create_database()

            else:
                self.exit_user()
                self.continue_greeting = False
                print(f"Exiting inventory system. Thank you.\n")

    def create_user(self):
        print(f"Creating new user ...")
        c = NewUser()
        c.create_user()
        print(c)
        c.add_user_db()

    def login_user(self):
        try:
            self.user_type = input('Enter user type: ')
            self.user_name = input('Enter user name: ')
        except:
            print(f'Invalid entry')
        l = UserTable()
        ut = l.authenticate_user(user_type=self.user_type,
                                 user_name=self.user_name)
        print(f"User type {ut} authenticated")
        if ut == 'manager':
            LabManager().menu()

    def create_database(self):
        d = NewTable()
        d.create_table(d.createtb_user)
        d.create_table(d.createtb_item)

    def exit_user(self):
        pass


def main():

    session = Inventory()


if __name__ == "__main__":
    main()
