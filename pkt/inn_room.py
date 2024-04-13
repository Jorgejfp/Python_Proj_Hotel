import mysql.connector
from pkt.connection import connectDB

class Room:
    def __init__(self, room_type, room_price, availability):
            self.id = None
            self.room_type = room_type
            self.room_price = room_price
            self.room_availability = availability
         
            def save_to_dbRoom(self):
                try:
                    # Connect to the database
                    connection = connectDB()

                    # Create a cursor object to execute SQL queries
                    cursor = connection.cursor()

                    # Prepare the SQL query to insert a new room
                    query = "INSERT INTO rooms (room_type, room_price, room_availability) VALUES (%s, %s, %s)"
                    values = (self.room_type, self.room_price, self.room_availability)

                    # Execute the query
                    cursor.execute(query, values)

                    # Commit the changes to the database
                    connection.commit()

                    # Close the cursor and connection
                    cursor.close()
                    connection.close()

                    print("New room added successfully!")
                except mysql.connector.Error as error:
                    print(f"Failed to add new room: {error}")
                    
                def update_in_dbRoom(self):
                    try:
                        # Connect to the database
                        connection = connectDB()

                        # Create a cursor object to execute SQL queries
                        cursor = connection.cursor()

                        # Prepare the SQL query to update an existing room
                        query = "UPDATE rooms SET room_type = %s, room_price = %s, room_availability = %s WHERE id = %s"
                        values = (self.room_type, self.room_price, self.room_availability, self.id)

                        # Execute the query
                        cursor.execute(query, values)

                        # Commit the changes to the database
                        connection.commit()

                        # Close the cursor and connection
                        cursor.close()
                        connection.close()

                        print("Room updated successfully!")
                    except mysql.connector.Error as error:
                        print(f"Failed to update room: {error}")
                        
                def delete_from_dbRoom(self):
                    try:
                        # Connect to the database
                        connection = connectDB()

                        # Create a cursor object to execute SQL queries
                        cursor = connection.cursor()

                        # Prepare the SQL query to delete a room
                        query = "DELETE FROM rooms WHERE id = %s"
                        values = (self.id,)

                        # Execute the query
                        cursor.execute(query, values)

                        # Commit the changes to the database
                        connection.commit()

                        # Close the cursor and connection
                        cursor.close()
                        connection.close()

                        print("Room deleted successfully!")
                    except mysql.connector.Error as error:
                        print(f"Failed to delete room: {error}")
                        
                def list_rooms():   
                    try:
                        # Connect to the database
                        connection = connectDB()

                        # Create a cursor object to execute SQL queries
                        cursor = connection.cursor()

                        # Prepare the SQL query to retrieve all rooms
                        query = "SELECT * FROM rooms"

                        # Execute the query
                        cursor.execute(query)

                        # Fetch all the results
                        rooms = cursor.fetchall()

                        # Display the results
                        for room in rooms:
                            print(room)

                        # Close the cursor and connection
                        cursor.close()
                        connection.close()
                    except mysql.connector.Error as error:
                        print(f"Failed to list rooms: {error}")
                        
            def update_availability(self, availability):
                try:
                    # Connect to the database
                    connection = connectDB()

                    # Create a cursor object to execute SQL queries
                    cursor = connection.cursor()

                    # Prepare the SQL query to update the availability of a room
                    query = "UPDATE rooms SET room_availability = %s WHERE id = %s"
                    values = (availability, self.id)

                    # Execute the query
                    cursor.execute(query, values)

                    # Commit the changes to the database
                    connection.commit()

                    # Close the cursor and connection
                    cursor.close()
                    connection.close()

                    print("Room availability updated successfully!")
                except mysql.connector.Error as error:
                    print(f"Failed to update room availability: {error}")
                    
                    def decrease_availability(self):
                        try:
                            # Connect to the database
                            connection = connectDB()

                            # Create a cursor object to execute SQL queries
                            cursor = connection.cursor()

                            # Prepare the SQL query to decrease the availability of a room
                            query = "UPDATE rooms SET room_availability = room_availability - 1 WHERE id = %s"
                            values = (self.id,)

                            # Execute the query
                            cursor.execute(query, values)

                            # Commit the changes to the database
                            connection.commit()

                            # Close the cursor and connection
                            cursor.close()
                            connection.close()

                            print("Room availability decreased successfully!")
                        except mysql.connector.Error as error:
                            print(f"Failed to decrease room availability: {error}")

                    def increase_availability(self):
                        try:
                            # Connect to the database
                            connection = connectDB()

                            # Create a cursor object to execute SQL queries
                            cursor = connection.cursor()

                            # Prepare the SQL query to increase the availability of a room
                            query = "UPDATE rooms SET room_availability = room_availability + 1 WHERE id = %s"
                            values = (self.id,)

                            # Execute the query
                            cursor.execute(query, values)

                            # Commit the changes to the database
                            connection.commit()

                            # Close the cursor and connection
                            cursor.close()
                            connection.close()

                            print("Room availability increased successfully!")
                        except mysql.connector.Error as error:
                            print(f"Failed to increase room availability: {error}")
              