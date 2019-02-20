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

# count rows
cursor.execute('SELECT count(*) as total FROM tbhistoricoacesso')
for row in cursor:
    count = row[0]
print(count)

# write header
cursor.execute('{} {} {}'.format(select, 'LIMIT',  1))
with open(filename, "w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description])
print('write header!')

# write rows
for offset in range(0, count, batch_size):
    print(offset)
    cursor.execute('{} LIMIT {} OFFSET {}'.format(select, batch_size, offset))
    for row in cursor:
       with open(filename, "a", newline='') as csv_file:
           csv_writer = csv.writer(csv_file)
           csv_writer.writerows(cursor)
