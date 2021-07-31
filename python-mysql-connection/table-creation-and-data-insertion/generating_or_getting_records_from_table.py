import mysql.connector
from mysql.connector import Error

try:
    myconnection = mysql.connector.connect(host='localhost',
                                           user='root',
                                           password='ufm8637594',
                                           database='sales')
    if myconnection.is_connected():

        # We can use different queries for generating the result such as order-by, where, fetching required records etc.

        query_for_selecting_records = """Select * from laptop"""
        cursor = myconnection.cursor()
        cursor.execute(query_for_selecting_records)

        # to get all the records:

        records=cursor.fetchall()
        for record in records:
            print(record)

        print("Total no.of rows in table: ", cursor.rowcount)

except Error as e:
    print('Error while generating the records from table'.format(e))
finally:
    if myconnection.is_connected():
        cursor.close()
        myconnection.close()
        print('Connection is closed')
