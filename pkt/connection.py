import mysql.connector

try:
    connectDB = mysql.connector.connect(user='root', password='', host='localhost', database='inn_reservation', port='3306')
    print("Connection to the database successful!")
except mysql.connector.Error as err:
    print("Error connecting to the database:", err)
