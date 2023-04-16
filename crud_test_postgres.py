#!/usr/bin/python3

import postgres_conn


def crud_action():
    user_choice = input("\nSelect any of the following operations: \n1.Create New Record\n2.Delete Existing Record\n3.Edit a record\n4.Print the records\n")

    if user_choice == "1":
        create_record()
    elif user_choice == "2":
        delete_record()
    elif user_choice == "3":
        edit_record()
    elif user_choice == "4":
        read_record()
    else:
        print("Invalid choice!\n")
        crud_action()



def create_record():
    id = input("\nPlease enter ID: ")
    name = input("\nPlease enter NAME: ")
    postgres_conn.database_conn()
    postgres_conn.POSTGRES_CURSOR.execute('INSERT INTO test (id, name) VALUES (%s, %s)', (id, name))
    postgres_conn.POSTGRES_CONNECTION.commit()



def read_record():
    pass


def edit_record():
    pass


def delete_record():
    name = input("\nEnter name for delete: ")
    postgres_conn.database_conn()
    postgres_conn.POSTGRES_CURSOR.execute(f"DELETE FROM test WHERE name = '{name}';")
    postgres_conn.POSTGRES_CONNECTION.commit()
    print(f"\nSuccessfully deleted user {name}")
    #postgres_conn.POSTGRES_CURSOR.execute(f"select * from test where name = '{name}';")
    #variable = postgres_conn.POSTGRES_CURSOR.fetchone()
    #print(variable)



#create_record()
#delete_record()
crud_action()
