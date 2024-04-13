import mysql.connector
from pkt.connection import connectDB

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
        try:
            # Connect to the MySQL database
            db = mysql.connector.connect(user='root', password='', host='localhost', database='inn_reservation', port='3306')
            print("Connection to the database successful!")

            # Create a cursor object to execute SQL queries
            cursor = db.cursor()

            # Prepare the SQL query to select all customers from the table
            query = "SELECT * FROM inn_customer"

            # Execute the SQL query
            cursor.execute(query)

            # Fetch all the rows returned by the query
            rows = cursor.fetchall()

            # Print the customer data
            if rows:
                print("ID\tFirst Name\tLast Name\tEmail\t\t\tPhone Number")
                print("-" * 80)
                for row in rows:
                    print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}\t{row[4]}")
                print("-" * 80)
            else:
                print("No customers found.")

        except mysql.connector.Error as err:
            print("Error:", err)

        finally:
            # Close the cursor and database connection
            if 'cursor' in locals():
                cursor.close()
            if 'db' in locals() and db.is_connected():
                db.close()
