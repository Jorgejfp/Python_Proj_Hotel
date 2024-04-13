import mysql.connector
from pkt.connection import connectDB

class Customer:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number       
        
    def getCostumerId(self, phone_number): 
        try:
            # Connect to the MySQL database
            connCustomerDB = connectDB()
            # Create a cursor object to execute SQL queries
            cursor = connCustomerDB.cursor()

            # Prepare the SQL query to select a customer by phone number
            query = "SELECT * FROM inn_customer WHERE phone_number = %s"
            values = (phone_number,)

            # Execute the SQL query
            cursor.execute(query, values)

            # Fetch the customer data
            customer_data = cursor.fetchone()

            # Close the cursor and database connection
            cursor.close()
           

            # If the customer data is found, create a Customer object and return it
            if customer_data:
                customer = Customer(customer_data[1], customer_data[2], customer_data[3], customer_data[4])
                customer.id = customer_data[0]
                return customer
            else:
                return None

        except mysql.connector.Error as err:
            print("Error:", err)
            return None
        
    
    def save_to_dbCustomer(self):
        # Connect to the MySQL database
        connCustomerDB = connectDB()
        # Create a cursor object to execute SQL queries
        cursor = connCustomerDB.cursor()

        # Prepare the SQL query to insert customer data into the table
        query = "INSERT INTO inn_customer (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s)"
        values = (self.first_name, self.last_name, self.email, self.phone_number)

        # Execute the SQL query
        cursor.execute(query, values)

        # Commit the changes to the database
        connCustomerDB.commit()

        # Close the cursor and database connection
        cursor.close()
    
        
        print("Customer data saved successfully!")
        
    def update_in_dbCustomer(self):
        # Connect to the MySQL database
        connCustomerDB = connectDB()
        # Create a cursor object to execute SQL queries
        cursor = connCustomerDB.cursor()

        # Prepare the SQL query to update customer data in the table
        query = "UPDATE inn_customer SET first_name = %s, last_name = %s, email = %s, phone_number = %s WHERE id = %s"
        values = (self.first_name, self.last_name, self.email, self.phone_number, self.id)

        # Execute the SQL query
        cursor.execute(query, values)

        # Commit the changes to the database
        connCustomerDB.commit()

        # Close the cursor and database connection
        cursor.close()
       

        print("Customer data updated successfully!")
        
    def delete_from_dbCustomer(self):
        # Connect to the MySQL database
        connCustomerDB = connectDB()
        # Create a cursor object to execute SQL queries
        cursor = connCustomerDB.cursor()

        # Prepare the SQL query to delete customer data from the table
        query = "DELETE FROM inn_customer WHERE id = %s"
        values = (self.id,)

        # Execute the SQL query
        cursor.execute(query, values)

        # Commit the changes to the database
        connCustomerDB.commit()

        # Close the cursor and database connection
        cursor.close()
      

        print("Customer data deleted successfully!")
        

    def list_customers():
        try:
            # Connect to the MySQL database
            connCustomerDB = connectDB
            print("Connection to the database successful!")

            # Create a cursor object to execute SQL queries
            cursor = connCustomerDB.cursor()

            # Prepare the SQL query to select all customers from the table
            query = "SELECT * FROM inn_customer"

            # Execute the SQL query
            cursor.execute(query)

            # Fetch all the rows returned by the query
            rows = cursor.fetchall()

            # Close the cursor and database connection
            cursor.close()
       

            # Return the fetched rows
            return rows

        except mysql.connector.Error as err:
            print("Error:", err)
            return []