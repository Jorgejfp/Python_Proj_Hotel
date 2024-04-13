from connection import connectDB

import mysql.connector

class Customer:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def save_to_dbCustomer(self):
        # Connect to the MySQL database
        db = connectDB()
        # Create a cursor object to execute SQL queries
        cursor = db.cursor()

        # Prepare the SQL query to insert customer data into the table
        query = "INSERT INTO inn_customer (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s)"
        values = (self.first_name, self.last_name, self.email, self.phone_number)

        # Execute the SQL query
        cursor.execute(query, values)

        # Commit the changes to the database
        db.commit()

        # Close the cursor and database connection
        cursor.close()
        db.close()
        
        print("Customer data saved successfully!")
        
    def update_in_dbCustomer(self):
        # Connect to the MySQL database
        db = connectDB()
        # Create a cursor object to execute SQL queries
        cursor = db.cursor()

        # Prepare the SQL query to update customer data in the table
        query = "UPDATE inn_customer SET first_name = %s, last_name = %s, email = %s, phone_number = %s WHERE id = %s"
        values = (self.first_name, self.last_name, self.email, self.phone_number, self.id)

        # Execute the SQL query
        cursor.execute(query, values)

        # Commit the changes to the database
        db.commit()

        # Close the cursor and database connection
        cursor.close()
        db.close()

        print("Customer data updated successfully!")
        
    def delete_from_dbCustomer(self):
        # Connect to the MySQL database
        db = connectDB()
        # Create a cursor object to execute SQL queries
        cursor = db.cursor()

        # Prepare the SQL query to delete customer data from the table
        query = "DELETE FROM inn_customer WHERE id = %s"
        values = (self.id,)

        # Execute the SQL query
        cursor.execute(query, values)

        # Commit the changes to the database
        db.commit()

        # Close the cursor and database connection
        cursor.close()
        db.close()

        print("Customer data deleted successfully!")
        
    
    def list_customers():
        # Connect to the MySQL database
        db = connectDB()
        # Create a cursor object to execute SQL queries
        cursor = db.cursor()

        # Prepare the SQL query to select all customers from the table
        query = "SELECT * FROM inn_customer"

        # Execute the SQL query
        cursor.execute(query)

        # Fetch all the rows returned by the query
        rows = cursor.fetchall()

        # Print the customer data
        for row in rows:
            print("ID:", row[0])
            print("First Name:", row[1])
            print("Last Name:", row[2])
            print("Email:", row[3])
            print("Phone Number:", row[4])
            print("--------------------")

        # Close the cursor and database connection
        cursor.close()
        db.close()