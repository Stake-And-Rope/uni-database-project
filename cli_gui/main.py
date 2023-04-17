#!/usr/bin/python3


import argparse
from PyInquirer import prompt
from prompt_toolkit.validation import Validator, ValidationError

#class MainApp(Validator):

main_menu = [
    {
        'type' : 'list',
        'name' : 'main_menu',
        'message' : 'Welcone to Uni Project Database',
        'choices' : ["Login", "Register", "Reset Password", "Contact", "Help", "Quit"]
    }
]


def main():
    answers = prompt(main_menu)
    if answers.get("main_menu") == "Login":
        print("I will Login")
    elif answers.get("main_menu") == "Register":
        print("I will create new accounn")
    elif answers.get("main_menu") == "Reset Password":
        print("I will reset the password")
    elif answers.get("main_menu") == "Contact":
        print("I will contact you")
    elif answers.get("main_menu") == "Help":
        print("I will help you")
    elif answers.get("main_menu") == "Quit":
        print("Goodbye!")


if __name__ == "__main__":
    main()




