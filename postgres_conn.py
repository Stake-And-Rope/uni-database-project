import logging

import psycopg2
import sshtunnel
from sshtunnel import SSHTunnelForwarder
from getpass import getpass


LINUX_USERNAME = input("Enter your username for Linux Linode Server: ")
LINUX_USER_PASSWD = getpass("Enter your user password: ")
print("\n")
POSTGRES_USERNAME = input("Enter PostgreSQL username: ")
POSTGRES_USER_PASSWD = getpass("Enter PostgreSQL user password: ")
print("\n")

POSTGRES_CURSOR = ''
POSTGRES_CONNECTION = ''


def database_conn(verbose = False):

    global POSTGRES_CURSOR
    global POSTGRES_CONNECTION
    # This function with create SSH Tunnel to the Linux Linode Server with custom credentials.
    # Before using the connector disable the SSH Passphrase on your local machine with `ssh-keygen -p` and set new blank passphrase. <-- To be fixed with more reliable solution

    if verbose:
        sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG

    global tunnel

    try:
        tunnel = SSHTunnelForwarder(
                ('139.144.178.197', 22),
                ssh_username = str(LINUX_USERNAME),
                ssh_password = str(LINUX_USER_PASSWD),
                remote_bind_address = ('127.0.0.1', 5432)
                )
        tunnel.start()
        print(f"SSH connection established successfully!\n")
    except (Exception) as error:
        print("SSH connection not established!\n")


    # Connect to PostgreSQL database with custom credentials.
    # Simple query is executed to display PostgreSQL vesrion.
    db_conn = psycopg2.connect(
            user = str(POSTGRES_USERNAME),
            password = str(POSTGRES_USER_PASSWD),
            host = "139.144.178.197",
            port = "5432",
            dbname = "uniproject"
            )
    cursor = db_conn.cursor()
    print("PostgreSQL database version: ")
    cursor.execute("SELECT version()")
    db_version = cursor.fetchone()
    print(db_version)

    POSTGRES_CURSOR = cursor
    POSTGRES_CONNECTION = db_conn

#        cursor.execute("INSERT INTO test (id, name) VALUES (%s, %s)", ("456654", "Gosho"))
#        db_conn.commit()
#        cursor.close()
#        db_conn.close()


#    except (Exception, Error) as error:
#        print("Error in connectin the PostgreSQL Database", error)


def close_ssh_tunnel():
    # Close the SSH Tunnel
    tunnel.close()

def close_sql_connection():
    # Close the connection to the PostgreSQL
    db_conn.close()

database_conn()



