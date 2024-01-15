import pandas as pd
import logging
import pymysql
import sshtunnel
from sshtunnel import SSHTunnelForwarder

# Configuración de SSH
ssh_host = '4.231.12.44'
ssh_username = 'ZeldaHaters'
ssh_password = 'Abc1234567890'
database_username = 'admin'
database_password = 'admin'
database_name = 'Projecto'
localhost = '127.0.0.1'

# Comando SQL que deseas ejecutar
def open_ssh_tunnel(verbose=False):
    if verbose:
        sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG
    
    global tunnel
    tunnel = SSHTunnelForwarder(
        (ssh_host, 22),
        ssh_username = ssh_username,
        ssh_password = ssh_password,
        remote_bind_address = ('127.0.0.1', 3306)
    )
    
    tunnel.start()

def mysql_connect():
    global connection
    connection = pymysql.connect(
        host='127.0.0.1',
        user=database_username,
        passwd=database_password,
        db=database_name,
        port=tunnel.local_bind_port
    )

def run_query(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = [list(row) for row in cursor.fetchall()]
    return result

def mysql_disconnect():
    connection.close()

def close_ssh_tunnel():
    tunnel.close

try:
    open_ssh_tunnel()
    mysql_connect()
    result_list = run_query("SELECT * FROM game")
    print("Tipo de Resultado:", type(result_list))
    print(result_list)
finally:
    mysql_disconnect()
    close_ssh_tunnel()

