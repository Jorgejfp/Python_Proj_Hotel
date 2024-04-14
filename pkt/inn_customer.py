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
        connCustomerDB = connectDB()
        if connCustomerDB is not None:
            try:
            
                # Create a cursor object to execute SQL queries
                cursor = connCustomerDB.cursor()
                # Prepare the SQL query to insert customer data into the table
                query = "INSERT INTO inn_customer (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s)"
                values = (self.first_name, self.last_name, self.email, self.phone_number)
                # Execute the SQL query
                cursor.execute(query, values)
                # Commit the changes to the database
                connCustomerDB.commit()
                
                print("Customer data saved successfully!")
            except Exception as e:
                print(f"Error when saving customer data: {e}")
                connCustomerDB.rollback() # Rollback the changes if an error occurs
            finally:
                # Close the cursor and database connection
                cursor.close()
                connCustomerDB.close()
        else:    
            
            print("Error: Could not connect to database")
        
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
    '''
    def delete_customer(customer_id, cursor, connection):
        
        try:
            # Prepare the SQL query to delete customer data from the table
            query = "DELETE FROM inn_customer WHERE id = %s"
            cursor.execute(query, (customer_id,))

            # Commit the changes to the database
            connection.commit()

            print("Customer data deleted successfully!")
        except Exception as e:
            print(f"Error when deleting customer data: {e}")
            connection.rollback()  # Rollback the changes if an error occurs finally:
        finally:
            cursor.close()
    '''        
    def list_customers():
        # Connect to the MySQL database
        connCustomerDB = connectDB()
        cursor = None  # Inicializar cursor a None fuera del bloque try
        try:
            # Verificar si la conexión se ha establecido correctamente 
            if connCustomerDB is not None:
                
                    # Create a cursor object to execute SQL queries
                    cursor = connCustomerDB.cursor()

                    # Prepare the SQL query to select all customers from the table
                    query = "SELECT * FROM inn_customer"

                    # Execute the SQL query
                    cursor.execute(query)

                    # Fetch all the rows returned by the query
                    customers = cursor.fetchall()
                    
                    for customer in customers:
                        print(customer) # Imprimir cada registro de cliente
                        
            else:
                print("Error: No se pudo conectar a la base de datos")
        except Exception as e:
                    print(f"Error al listar clientes: {e}")  
        finally:
            # Cerrar el cursor y la conexión a la base de datos si el cursor se ha inicializado correctamente
            if cursor is not None: 
                cursor.close()
            if connCustomerDB is not None:
                connCustomerDB.close()
    
                
                
    def delete_customer_by_id(customer_id):
        # Connect to the database
        connCustomerDB = connectDB()
        cursor = None

        try:
            if connCustomerDB is not None:
                cursor = connCustomerDB.cursor()

                # Check if the customer ID exists in the database
                query = "SELECT first_name, last_name, email, phone_number FROM inn_customer WHERE id = %s"
                cursor.execute(query, (customer_id,))
                customer_data = cursor.fetchone()
                                
            else:
                print("Error: Could not connect to database")
        except Exception as e:
            print(f"Error when deleting customer data: {e}")
            if connCustomerDB is not None:
                connCustomerDB.rollback()  # Rollback the changes if an error occurs
        finally:
            if cursor is not None:
                cursor.close()
            if connCustomerDB is not None:
                connCustomerDB.close()