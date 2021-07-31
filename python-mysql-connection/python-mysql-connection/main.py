# A "connectionexample" database is created in Mysql, and we are going to establish connection between Mysql and Python.

# Step:1 Import mysql.connector library.
import mysql.connector

# Catch exceptions/: that may occur during this process by importing the Error class from the MySQL connector module
# using a from mysql.connector import Error statement. Error class is useful to debug when we failed to connect to
# MySQL. For example, ACCESS DENIED ERROR when the username or password is wrong. The connect() method can throw a
# Database error exception if one of the required parameters is wrong. For example, if you provide a database name
# that is not present in MySQL.

# Step:2 import Error statement for  Catch Exceptions
from mysql.connector import Error

# Step:3 (optional) Use try-catch for error handling

try:
    # Step:4 Use the connect() method: Use the connect() method of the MySQL Connector class with the required
    # arguments to connect MySQL. It would return a MySQLConnection object if the connection established successfully
    connection = mysql.connector.connect(host='localhost',
                                         database='connectionexample',
                                         user='root',
                                         password='ufm8637594')
    if connection.is_connected():

        # connection.get_server_info() is used to return database/server information/version

        databaseinfo = connection.get_server_info()
        print("Connected to MYSQL version", databaseinfo)

        # Step:5 Use the cursor() method of a MySQLConnection object to create a cursor object to perform various SQL
        # operations.

        cursor = connection.cursor()

        # Step:6 The execute() methods run the SQL query and return the result.
        cursor.execute("select database();")

        # Step:7 Extract result using fetchall():
        # Use cursor.fetchall() or fetchone() or fetchmany() to read query result.

        record = cursor.fetchall()
        print("You are connected to the database:", record)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():

        # Step:8 Close cursor and connection objects:
        # use cursor.clsoe() and connection.clsoe() method to close open connections after your work completes

        cursor.close()
        connection.close()
        print("MySQL connection is closed")
