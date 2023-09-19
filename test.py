import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  auth_plugin='mysql_native_password',
  database='qubes_updated_data'
)

print(mydb)