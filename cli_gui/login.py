#!/usr/bin/python3

import sys
sys.path.append(r'..')
import crud_test_postgres, postgres_conn

from PyInquirer import prompt
from prompt_toolkit.validation import Validator, ValidationError
import main, custom_style


login_menu = [
    {
        'type' : 'list',
        'name' : 'login_menu',
        'message' : 'Login into Uni Project Database',
        'choices' : ["Login", "Go back to Main Menu"]
    }

]



def login():
    answers = prompt(login_menu, style = custom_style.style)
    if answers.get("login_menu") == "Login":
        print(f"\nEnter your Server and Database Credentials:\n")
        postgres_conn.database_conn()
        crud_test_postgres.crud_action()
    elif answers.get("login_menu") == "Go back to Main Menu":
        #print("I will go back to the Main Menu")
        main.main()


if __name__ == "__main__":
    login()
