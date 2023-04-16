#!/usr/bin/python3

import postgres_conn

def create_record():
    postgres_conn.database_conn()
    postgres_conn.POSTGRES_CURSOR.execute("INSERT INTO test (id, name) VALUES (%s, %s)", ("001100", "Maria"))
    postgres_conn.POSTGRES_CONNECTION.commit()



def read_record():
    pass


def edit_record():
    pass


def delete_record():
    pass


create_record()
