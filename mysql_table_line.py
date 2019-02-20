import mysql.connector
import csv

config = {
        'host': '',
        'port': 3306,
        'database': '',
        'user': '',
        'password': '',
        'charset': 'utf8',
        'use_unicode': True,
        'get_warnings': True,
    }

db = mysql.connector.Connect(**config)

batch_size = 1000
filename = "out.csv"
select = 'SELECT * FROM tbhistoricoacesso'
cursor = db.cursor()

cursor.execute(select)
for row in cursor:
   print(row)
   with open(filename, "w", newline='') as csv_file:
       csv_writer = csv.writer(csv_file)
       csv_writer.writerow([i[0] for i in cursor.description]) # write headers
       csv_writer.writerows(cursor)
