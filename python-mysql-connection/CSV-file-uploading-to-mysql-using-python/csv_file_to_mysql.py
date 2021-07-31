# How to connect to mysql using python and import the csv file into mysql and create a table?


import mysql.connector
# Step:1
import pandas as pd
from mysql.connector import Error

# Step:2
empdata = pd.read_csv("US-employee-file.csv", index_col=False, delimiter=",")
print('Reading CSV file using Pandas pd...')
empdata.head()

try:
    # Step:3
    myconnection = mysql.connector.connect(host='localhost', user='root', password='ufm8637594')
    if myconnection.is_connected():
        query_for_selecting_records = """Select * from csvfileuploadingusingpython.employee_data"""
        cursor = myconnection.cursor()
        cursor.execute("CREATE DATABASE csvfileuploadingusingpython;")
        print("Database is created..")
        # cursor.execute("Select database();")
        # record = cursor.fetchone()
        # print("You are connected to:", record)

        # Query to drop any table that may exist in the given database:
        cursor.execute('DROP TABLE IF EXISTS csvfileuploadingusingpython.employee_data;')
        # Create the new table with name: employee_data
        cursor.execute('CREATE TABLE csvfileuploadingusingpython.employee_data(first_name varchar(255),last_name '
                       'varchar(255),company_name '
                       'varchar(255),address varchar(255),city varchar(255),county varchar(255),state varchar(255),'
                       'zip int,phone1 varchar(255),phone2 varchar(255),email varchar(255),web varchar(255))')
        print("Table is created....")
        # iterate through the Dataframes/Records
        for i, row in empdata.iterrows():
            sql_query_for_csv_records_insertion = """INSERT INTO csvfileuploadingusingpython.employee_data VALUES (%s,
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """
            cursor.execute(sql_query_for_csv_records_insertion, tuple(row))
            print('Record inserted...')
            # To permanently commit changes, use commit()
            myconnection.commit()
        cursor.execute(query_for_selecting_records)
        # to get all the records:
        records = cursor.fetchall()
        for record in records:
            print(record)

        print("Total no.of rows in table: ", cursor.rowcount)


except Error as e:
    print('Error while Uploading CSV file:'.format(e))
finally:
    if myconnection.is_connected():
        cursor.close()
        myconnection.close()
        print('Connection is closed')
