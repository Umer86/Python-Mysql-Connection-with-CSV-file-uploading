import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='ufm8637594',
                                         database='sales')

    if connection.is_connected():
        mySql_create_table_query = """CREATE TABLE Laptop(
                             Id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
                             Name varchar(250) NOT NULL,
                             Price float NOT NULL,
                             Purchase_date Date NOT NULL)"""
        cursor = connection.cursor()
        result = cursor.execute(mySql_create_table_query)
        print("Laptop Table created successfully ")
except Error as e:
    print("Failed to create table in MySQL: {}".format(e))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection is closed")
