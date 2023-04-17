#!/usr/bin/python3

from PyInquirer import prompt
from prompt_toolkit.validation import Validator, ValidationError
import main, custom_style



login_menu = [
    {
        'type' : 'list',
        'name' : 'login_menu',
        'message' : 'Login into Uni Project Database',
        'choices' : ["Login as a student", "Login as a professor", "Login as a Admin", "Go back to Main Menu"]
    }

]



def login():
    answers = prompt(login_menu, style = custom_style.style)
    if answers.get("login_menu") == "Login as a student":
        print("I will login as a student")
    elif answers.get("login_menu") == "Login as a professor":
        print("I will login as a professor")
    elif answers.get("login_menu") == "Login as a Admin":
        print("I will login as a Admin")
    elif answers.get("login_menu") == "Go back to Main Menu":
        print("I will go back to the Main Menu")
        main.main()


if __name__ == "__main__":
    login()
