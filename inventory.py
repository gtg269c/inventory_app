"""main page for the inventory app
"""

import os
from src.user import User, NewUser
from src.database import UserTable, NewTable


class Login():
    def __init__(self) -> None:
        self.user_name


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
        l = UserTable()
        l.authenticate_user

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
