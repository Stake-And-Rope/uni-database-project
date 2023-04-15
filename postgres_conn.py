#!/usr/bin/python3
import psycopg2
from sshtunnel import SSHTunnelForwarder
from getpass import getpass


USERNAME = input("Enter your username for Linux Linode Server: ")
USER_PASSWD = getpass("Enter your user password: ")


def open_ssh_tunnel(verbose = False):

    # This fucntion with create SSH Tunnel to the Linux Linode Server. 
    # Before using the connector disable the SSH Passphrase on your local machine `ssh-keygen -p` and set new blank passphrase. <-- To be fixed with more reliable solution

    if verbose:
        sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG


    global tunnel
    tunnel = SSHTunnelForwarder(
            ('139.144.178.197', 22),
            ssh_username = str(USERNAME),
            ssh_password = str(USER_PASSWD),
            remote_bind_address = ('127.0.0.1', 5432)
            )
    tunnel.start()
    print(tunnel)

open_ssh_tunnel()
