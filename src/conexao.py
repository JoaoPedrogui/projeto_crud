import mysql
import mysql.connector 

conn = mysql.connector.connect(
    username = 'guimaraes',
    host = 'localhost',
    password = 'projeto123',
    db = 'projeto_crud'
)

if conn.is_connected():
    print("Conexão com o MySQL estabelecida!")
else:
    print("Falha na conexão com o MySQL.")

