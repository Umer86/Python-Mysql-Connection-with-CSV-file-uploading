import requests
import json
import mysql.connector
from mysql.connector import Error

my_api_key = '05BA8h52Ad3TDsG2IUyLUEMeRFpWqwMH'
my_api_url = "https://api.nytimes.com/svc/news/v3/content/all/all.json?api-key="+my_api_key
r = requests.get(my_api_url)
package_json = r.json()

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='apitodatabase',
                                         user='root',
                                         password='ufm8637594')
    databaseinfo = connection.get_server_info()
    print("Connected to MYSQL version", databaseinfo)

    if connection.is_connected():
        cursor = connection.cursor()
        for i in package_json['data']:
            t1=[]
            for x in i:
                valdata=validate_string(i.get(x,None))
                t1.append(valdata)
            #
            cursor.execute("""INSERT""")


except Error as e:
    print('Error while implementing:'.format(e))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
