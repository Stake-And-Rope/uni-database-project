#!/usr/bin/python3

import postgres_conn

def create_record():
    id = input("please enter ID: ")
    name = input("please enter NAME: ")
    postgres_conn.database_conn()
    postgres_conn.POSTGRES_CURSOR.execute('INSERT INTO test (id, name) VALUES (%s, %s)', (id, name))
    postgres_conn.POSTGRES_CONNECTION.commit()



def read_record():
    pass


def edit_record():
    pass


def delete_record():
    name = input("Enter name for delete: ")
    postgres_conn.database_conn()
    postgres_conn.POSTGRES_CURSOR.execute(f"DELETE FROM test WHERE name = '{name}';")
    postgres_conn.POSTGRES_CONNECTION.commit()
    print(f"\nSuccessfully deleted user {name}")
    #postgres_conn.POSTGRES_CURSOR.execute(f"select * from test where name = '{name}';")
    #variable = postgres_conn.POSTGRES_CURSOR.fetchone()
    #print(variable)



#create_record()
delete_record()
