#!/usr/bin/python3

import sys
sys.path.append(r'..')
import crud_test_postgres, postgres_conn

from PyInquirer import prompt
from prompt_toolkit.validation import Validator, ValidationError
import main, custom_style




main_menu = [
    {
        'type' : 'list',
        'name' : 'main_menu',
        'message' : 'Main Menu - Select any operation: ',
        'choices' : ["Create New Record", "Edit Existing Record", "Delete Existing Record", "Go back"]
    }

]




def mainmenu():
    answers = prompt(main_menu, style = custom_style.style)
    if answers.get("main_menu") == "Create New Record":
        print(f"I will create a new student!\n")
    elif answers.get("main_menu") == "Edit Existing Record":
        pass
    elif answers.get("main_menu") == "Delete Exisitng Record":
        pass
    elif answers.get("main_menu") == "Go back":
        main.main()


if __name__ == "__main__":
    mainmenu()
