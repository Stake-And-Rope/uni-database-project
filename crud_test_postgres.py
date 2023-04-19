#!/usr/bin/python3

import postgres_conn


def crud_action():
    user_choice = input("\nSelect any of the following operations: \n1.Create New Record\n2.Delete Existing Record\n3.Edit a record\n4.Print the entire table\n\n")

    if user_choice == "1":
        create_record()
    elif user_choice == "2":
        delete_record()
    elif user_choice == "3":
        edit_record()
    elif user_choice == "4":
        read_table()
    else:
        print("Invalid choice!\n")
        crud_action()

def create_record():
    id = input("\nPlease enter ID: ")
    name = input("\nPlease enter NAME: ")
    #postgres_conn.database_conn()
    postgres_conn.POSTGRES_CURSOR.execute('INSERT INTO test (id, name) VALUES (%s, %s)', (id, name))
    postgres_conn.POSTGRES_CONNECTION.commit()

def read_table():
    #postgres_conn.database_conn()
    postgres_conn.POSTGRES_CURSOR.execute(f"SELECT * FROM test")
    result = postgres_conn.POSTGRES_CURSOR.fetchall()
    for student_info in result:
        print(f"ID: {student_info[0]} -- Name: {student_info[1]}")

def edit_record():
    student_id = input("\nEnter the ID of existing student: ")
    #postgres_conn.database_conn()
    postgres_conn.POSTGRES_CURSOR.execute(f"SELECT * FROM test WHERE id = '{student_id}'")
    result = postgres_conn.POSTGRES_CURSOR.fetchone()
    new_name = input("\nEnter the new name: ")
    postgres_conn.POSTGRES_CURSOR.execute(f"UPDATE test SET name = '{new_name}' WHERE id = '{student_id}'")
    postgres_conn.POSTGRES_CONNECTION.commit()
    postgres_conn.POSTGRES_CURSOR.execute(f"SELECT * FROM test WHERE name = '{new_name}' AND id = '{student_id}'")
    result = postgres_conn.POSTGRES_CURSOR.fetchone()
    print(f"Student ID: {result[0]} -- Student Name: {result[1]}")

def delete_record():
    name = input("\nEnter name for delete: ")
    #postgres_conn.database_conn()
    postgres_conn.POSTGRES_CURSOR.execute(f"DELETE FROM test WHERE name = '{name}';")
    postgres_conn.POSTGRES_CONNECTION.commit()
    print(f"\nSuccessfully deleted user {name}")
    #postgres_conn.POSTGRES_CURSOR.execute(f"select * from test where name = '{name}';")
    #variable = postgres_conn.POSTGRES_CURSOR.fetchone()
    #print(variable)

#create_record()
#delete_record()
#crud_action()
