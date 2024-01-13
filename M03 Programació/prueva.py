import mysql.connector
from sshtunnel import SSHTunnelForwarder

ssh_config = {
   'ssh_address_or_host': ('4.231.12.44', 22),
   'ssh_username': 'ZeldaHaters',
   'ssh_password': 'Abc1234567890',
   }

mysql_config = {
   'user': 'root',
   'password': '123456',
   'host': 'localhost',
   'database': 'custprod',
   'port': 3306,
}


try:
   # Intenta establecer la conexión MySQL a través del túnel SSH
   connection = mysql.connector.connect(**mysql_config)
   print("Conexión a MySQL exitosa")


   # Puedes realizar operaciones en la base de datos aquí


except mysql.connector.Error as err:
   print(f"Error de MySQL: {err}")


finally:
   # Asegúrate de cerrar la conexión al finalizar
   if 'connection' in locals() and connection.is_connected():
       connection.close()
       print("Conexión cerrada")