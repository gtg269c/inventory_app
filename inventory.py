"""main page for the inventory app
"""

import os
from src.user import User, NewUser
from src.database import create_table


class Inventory():
    def __init__(self) -> None:
        self.greeting()

    def greeting(self):

        greeting_options = [
            (0, "create user"),
            (1, "login"),
            (2, "exit system"),
            (3, "create database")
        ]

        print(f"Welcome to the lab inventory system.")
        print(f"What will you like to do? (choose an option)")
        for key, value in greeting_options:
            print(f"Press {key} to {value}")
        user_input = int(input("choose an option: "))
        if user_input == 0:
            self.create_user()
        elif user_input == 1:
            self.login_user()
        elif user_input == 3:
            self.create_database
        else:
            self.exit_user()

    def create_user(self):
        print(f"Creating new user ...")
        c = NewUser.create_user()
        print(c)
        c.add_user_db()

    def login_user(self):
        pass

    def create_database(self):
        create_table

    def exit_user(self):
        pass


def main():

    session = Inventory()


if __name__ == "__main__":
    main()
