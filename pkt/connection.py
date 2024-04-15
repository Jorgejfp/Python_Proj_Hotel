import mysql.connector

def connectDB():
    
    try:
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='inn_reservation', port='3306')
        #print("Connection to the database successful!")
        if conn.is_connected():
        #    print("Connection successful!")
            return conn
        
    except mysql.connector.Error as err:
        print("Error connecting to the database:", err)
        
    return None
