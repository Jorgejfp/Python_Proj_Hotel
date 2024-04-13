import mysql.connector

connectDB = mysql.connector.connect(user='root', password='', host='localhost', database='inn_reservation', port='3306')

print(connectDB)
