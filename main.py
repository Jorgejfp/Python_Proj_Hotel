#There is a small local Inn near to the ocean named Pacific Inn that offers accommodation services to the customers. They need a reservation system to handle their business. You as 
# A developer is responsible to create a project based on Pacific Inn requirements.
# First, Pacific Inn has 4 types of rooms:
# 1- Standard rooms (S)
# 2- Premium rooms(P)
# 3- Ocean view rooms(O)
# 4- Economy rooms(E)
# Pacific has 1 Standard rooms, 5 Premium rooms,9 Economy rooms and 5 Ocean view ones.
# In this project you have number of costumers with their desire accommodation information that you need to make a reservation and complete check-in/out for Pacific Inn
# This project has following main functionalities
# 1- Some costumers make their reservation by phone and a receptionist saved customer request in a text file. So, the project must reserve room by reading a reservation information from a given file and save records in a database named Inn_reservation
# 2- When a customer wants to Check-out then LIRS must print out the customer accommodation information and free his/her room in the system.
# 3- It should have a mechanism to Check-in new customer with interactive question from console and save a new reservation in its database.
# 4- If all rooms are full, check-in process must be locked as if the user is not able to choose check-in option.
# In the next point you will see the schema of LIRS database that you will implement with MySql db.
# tables
# 1nn_customer
#     id int (PK)
#     first_name varchar(50)
#     last_name varchar(50)
#     email varchar(30)
#     phone_number bigint


# 1nn_rooms"""  """
#     id int (PK)
#     room_type varchar( 1)
#     room_price decimal(5,2)
#     availability smallint
#     cuc¡tomer_j c :id

# 1nn_reservation
#     id int (PK)
#     room_type int (FK)
#     customer id int (FK)
#     accommodation_days smallint
#     cost decimal(5,2)
#     checkout tinyint(1)


# Inn_rooms table stores all room information.
# Inn_customer table store costumer information.
# Inn_reservation is the most important table.
# It has relationships with 2 other tables.
# room_type and costumer_id are foreign keys
# In inn_reservation table.
# checkout data type in inn_reservation is tinyint that gets
# either 0 or 1 values.
# If value is 0 means the costumer has not been checked-out
# and he/she needs to pay for the service.
# If Value is 1 means the costumer has been successfully
# checked-out and he/she already paid for all services.
# Look at next page to see some records in each table.

import mysql.connector

# Connect to the MySQL database
cnx = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="Inn_reservation"
)

# Create a cursor object to interact with the database
cursor = cnx.cursor()

# Function to read reservation information from a file and save records in the database
def reserve_room(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # Parse the reservation information from the file
            reservation_info = line.strip().split(',')
            customer_id = int(reservation_info[0])
            room_type = reservation_info[1]
            accommodation_days = int(reservation_info[2])
            cost = float(reservation_info[3])
            
            # Check if the room is available
            cursor.execute("SELECT id FROM Inn_rooms WHERE room_type = %s AND availability > 0", (room_type,))
            room = cursor.fetchone()
            
            if room:
                room_id = room[0]
                
                # Insert the reservation into the database
                cursor.execute("INSERT INTO Inn_reservation (room_type, customer_id, accommodation_days, cost, checkout) VALUES (%s, %s, %s, %s, 0)", (room_id, customer_id, accommodation_days, cost))
                
                # Update the availability of the room
                cursor.execute("UPDATE Inn_rooms SET availability = availability - 1 WHERE id = %s", (room_id,))
                
                cnx.commit()
                print("Reservation successfully made.")
            else:
                print("No available rooms of type", room_type)

# Function to print customer accommodation information and free the room in the system
def check_out(customer_id):
    # Get the reservation information for the customer
    cursor.execute("SELECT r.id, c.first_name, c.last_name, r.accommodation_days, r.cost FROM Inn_reservation r JOIN Inn_customer c ON r.customer_id = c.id WHERE r.customer_id = %s AND r.checkout = 0", (customer_id,))
    reservation = cursor.fetchone()
    
    if reservation:
        reservation_id, first_name, last_name, accommodation_days, cost = reservation
        
        # Print the accommodation information
        print("Reservation ID:", reservation_id)
        print("Customer Name:", first_name, last_name)
        print("Accommodation Days:", accommodation_days)
        print("Total Cost:", cost)
        
        # Update the checkout status in the database
        cursor.execute("UPDATE Inn_reservation SET checkout = 1 WHERE id = %s", (reservation_id,))
        
        # Update the availability of the room
        cursor.execute("UPDATE Inn_rooms SET availability = availability + 1 WHERE id = (SELECT room_type FROM Inn_reservation WHERE id = %s)", (reservation_id,))
        
        cnx.commit()
        print("Check-out successful.")
    else:
        print("No active reservation found for customer ID", customer_id)

# Function to check-in a new customer and save a new reservation in the database
def check_in():
    # Check if all rooms are full
    cursor.execute("SELECT COUNT(*) FROM Inn_rooms WHERE availability > 0")
    available_rooms = cursor.fetchone()[0]
    
    if available_rooms == 0:
        print("All rooms are full. Check-in process is locked.")
    else:
        # Get customer information from the user
        first_name = input("Enter customer's first name: ")
        last_name = input("Enter customer's last name: ")
        email = input("Enter customer's email: ")
        phone_number = input("Enter customer's phone number: ")
        
        # Get the available room types
        cursor.execute("SELECT DISTINCT room_type FROM Inn_rooms WHERE availability > 0")
        room_types = cursor.fetchall()
        
        # Display the available room types to the user
        print("Available room types:")
        for room_type in room_types:
            print(room_type[0])
        
        # Get the desired room type from the user
        room_type = input("Enter desired room type: ")
        
        # Check if the desired room type is available
        cursor.execute("SELECT id FROM Inn_rooms WHERE room_type = %s AND availability > 0", (room_type,))
        room = cursor.fetchone()
        
        if room:
            room_id = room[0]
            
            # Get the number of accommodation days from the user
            accommodation_days = int(input("Enter number of accommodation days: "))
            
            # Calculate the cost based on the room type and accommodation days
            cursor.execute("SELECT room_price FROM Inn_rooms WHERE id = %s", (room_id,))
            room_price = cursor.fetchone()[0]
            cost = room_price * accommodation_days
            
            # Insert the new reservation into the database
            cursor.execute("INSERT INTO Inn_customer (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, phone_number))
            customer_id = cursor.lastrowid
            
            cursor.execute("INSERT INTO Inn_reservation (room_type, customer_id, accommodation_days, cost, checkout) VALUES (%s, %s, %s, %s, 0)", (room_id, customer_id, accommodation_days, cost))
            
            # Update the availability of the room
            cursor.execute("UPDATE Inn_rooms SET availability = availability - 1 WHERE id = %s", (room_id,))
            
            cnx.commit()
            print("Check-in successful.")
        else:
            print("No available rooms of type", room_type)

# Close the cursor and connection to the database
cursor.close()
cnx.close() 
