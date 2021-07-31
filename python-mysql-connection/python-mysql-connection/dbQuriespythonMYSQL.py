import mysql.connector
from mysql.connector import Error

try:
    username = input("Enter the Username: ")
    passd = input("Enter the Password: ")
    hosting = input("Enter the Host: ")

    myconnection = mysql.connector.connect(host=hosting,
                                           user=username,
                                           password=passd)

    if myconnection.is_connected():
        dbinfo = myconnection.get_server_info()
        print("Mysql Version:", dbinfo)
        cursor = myconnection.cursor()
        cursor.execute("CREATE DATABASE employer;")
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        print("List of databases as per query:", databases)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if myconnection.is_connected():
        cursor.close()
        myconnection.close()
        print("MySQL connection is closed")
