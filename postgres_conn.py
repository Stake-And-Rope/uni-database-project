from sshtunnel import SSHTunnelForwarder

with sshtunnel.SSHTunnelForwarder(
        ('139.144.178.197', 22),
        ssh_username = 'mariqn', ssh_password = 'glavuta1',
        ) as server:
            server.start()
