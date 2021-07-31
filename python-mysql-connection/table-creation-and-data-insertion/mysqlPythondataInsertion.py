import mysql.connector
from mysql.connector import Error

try:
    connection=mysql.connector.connect(host='localhost',
                                       user='root',
                                       password='ufm8637594',
                                       database='sales')
    if connection.is_connected():
        mysql_data_insertion_query="""INSERT INTO Laptop (Name, Price, Purchase_date) 
                           VALUES (%s, %s, %s)"""
        records = [('MacBook Pro', 2499, '2019-06-20'),
                   ('Area 51M', 6999, '2019-04-14'),
                   ('HP Pavilion Power', 1999, '2019-01-11'),
                   ('MSI WS75 9TL-496', 5799, '2019-02-27'),
                   ('Microsoft Surface', 2330, '2019-07-23')]
        cursor=connection.cursor()

        # To execute insertion of multiple rows/records then executemany() method is used.

        result=cursor.executemany(mysql_data_insertion_query, records)

        # Commit your changes: After the successful execution of a query make changes persistent into a database
        # using the commit() of a connection class.
        connection.commit()
        print(cursor.rowcount, "Records are inserted to the table")
except Error as e:
    print("Data cannot be inserted in table".format(e))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection is closed")
