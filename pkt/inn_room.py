import mysql.connector
from pkt.connection import connectDB

class Room:
    def __init__(self, room_type, room_price, availability):
            self.id = None
            self.room_type = room_type
            self.room_price = room_price
            self.room_availability = availability
            
            
            
    def list_rooms():   
            try:
                # Connect to the database
                connection = connectDB()

                # Create a cursor object to execute SQL queries
                cursor = connection.cursor()

                # Prepare the SQL query to retrieve all rooms
                query = "SELECT * FROM inn_rooms"

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
                    
    def get_total_available_rooms():
        try:
            # Connect to the database
            connection = connectDB()

            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Prepare the SQL query to retrieve the total available rooms
            query = "SELECT COUNT(*) FROM rooms WHERE room_availability > 0"

            # Execute the query
            cursor.execute(query)

            # Fetch the result
            total_available_rooms = cursor.fetchone()[0]

            # Close the cursor and connection
            cursor.close()
            connection.close()

            return total_available_rooms
        except mysql.connector.Error as error:
            print(f"Failed to get total available rooms: {error}")
            
    
    def check_availability(self):
            try:
                # Connect to the database
                connection = connectDB()

                # Create a cursor object to execute SQL queries
                cursor = connection.cursor()

                # Prepare the SQL query to check the availability of a room based on room_type
                query = "SELECT room_availability FROM rooms WHERE room_type = %s"
                values = (self.room_type,)

                # Execute the query
                cursor.execute(query, values)

                # Fetch the result
                availability = cursor.fetchone()

                # Close the cursor and connection
                cursor.close()
                connection.close()

                if availability:
                    return availability[0] > 0
                else:
                    return False
            except mysql.connector.Error as error:
                print(f"Failed to check room availability: {error}")
                return False
                
                    
           