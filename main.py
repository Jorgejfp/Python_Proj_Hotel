from mysql.connector import Error as MySQLError
from pkt import inn_customer, inn_room, inn_reservation
from pkt.inn_customer import Customer
from pkt.inn_room import Room
from pkt.inn_reservation import Reservation
from pkt.connection import connectDB
import os


#conectar a la base de datos
try:
    connection = connectDB()
    
    if connection.is_connected():
        print("Database connection established")
        try:
                with open("reservation_file.txt", "r") as f1:
                    cursor = connection.cursor()
                

                    for line in f1.readlines():
                        data = line.strip().split(",")
                        accommodation_days = data[5]  # The duration of the reservation is in the last position of the data

                        # Create a new Customer object with the data from lines position 0, 1, 2, 3
                        cursor.execute("INSERT INTO inn_customer (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s)", (data[0], data[1], data[2], data[3]))
                        
                        #Search for the last added ID                        
                        customer_id = cursor.lastrowid
                        # Search for the ID associated with the room type
                        room_type = Room.getID(data[4])
                    
                        #Insert data into the reservation table
                        cursor.execute("INSERT INTO inn_reservation (room_type, customer_id, accommodation_days) VALUES (%s, %s, %s)", 
                                    (room_type, customer_id, accommodation_days))    
                        # Commit to confirm the transactions in the database.
                        connection.commit()
                        
                    print("Reservation data successfully inserted into the database")   
                    
                    # Remove the file after reading
                    #os.remove("reservation_file.txt")
                

        except FileNotFoundError:
                print("The reservation_file.txt file was not found.")
                
except MySQLError as error:
    print(f"Error connecting to the database: {error}")
    
finally:
   
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Database connection closed")


#Definicion de funciones

def create_customer():
    print("Enter customer details:")
    # Code to create a new customer
    first_name = input("Enter customer's first name: ")
    last_name = input("Enter customer's last name: ")
    email = input("Enter customer's email: ")
    phone_number = input("Enter customer's phone number: ")
    
    # Create a new customer object
    customer = inn_customer.Customer(first_name, last_name, email, phone_number)
    
    # Save the customer to the database
    customer.save_to_dbCustomer()
    pass

def update_customer():
    customer_id = input("Enter customer ID: ")
    
    # Try to retrieve the customer by ID
    customer = inn_customer.Customer.get_customer_by_id(customer_id)
    
    # Check if the customer object is valid1
    if customer:
        # Print customer details
        print("\nCustomer Details:")
        customer.print_customer_details2()
        
        # Prompt the user to enter updated information
        first_name = input("\nEnter updated first name: ")
        last_name = input("Enter updated last name: ")
        email = input("Enter updated email: ")
        phone_number = input("Enter updated phone number: ")
        
        # Update the customer's information directly
        customer.id = customer_id
        customer.first_name = first_name
        customer.last_name = last_name
        customer.email = email
        customer.phone_number = phone_number
        
        # Save the updated information to the database
        customer.update_in_dbCustomer()
        
        print("\nCustomer updated successfully!")
    else:
        print("\nCustomer not found. Please check the customer ID.")


# Definition of Main Menu
def print_header(menu_name):
    clear_screen()
    print("*" * 77)
    print("*" + " " * 24 + "Welcome to the LIRS System" + " " * 25 + "*")
    print("*" * 77)
    print("Please enter a number related to the following options to continue:")
    print("-" * 77)
    print("{:^77}".format("Options of " + menu_name + " Menu"))
    print("-" * 77)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def main_menu():
    while True:
        print_header("Main Menu")
        print("1. Menu Customer")
        print("2. Menu Room")
        print("3. Menu Reservation")
        print("4. Exit\n\n")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            menu_customers()
        elif choice == "2":
            menu_room()
        elif choice == "3":
            menu_reservation()
        elif choice == "4":
            print("Are you sure you want to exit? (Y/N)")
            confirm = input("Enter your choice: ")
            if confirm.lower() == "y":
                print("Exiting...")
                break
            break
        else:
            print("Invalid choice. Please try again.")
        

#frm_customer = form customer
def print_header(menu_name):
    clear_screen()
    print("*" * 77)
    print("*" + " " * 24 + "Welcome to the LIRS System" + " " * 25 + "*")
    print("*" * 77)
    print("Please enter a number related to the following options to continue:")
    print("-" * 77)
    print("{:^77}".format("Options of " + menu_name + " Menu"))
    print("-" * 77)
    
def menu_customers():
    while True:
        print_header("Customer")
        print("1. Create Customer")
        print("2. Update Customer")
        print("3. Delete Customer")
        print("4. List Customers")
        print("5. Back to Main Menu\n\n")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_customer()
        elif choice == "2":
            update_customer()
        elif choice == "3":
            customer_id = int(input("Enter the ID of the customer you want to delete: "))         
            customerDelete = inn_customer.Customer.delete_customer_by_id(customer_id)     
        elif choice == "4":
            customers = inn_customer.Customer.list_customers()         
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def print_header(menu_name):
    clear_screen()
    print("*" * 77)
    print("*" + " " * 24 + "Welcome to the LIRS System" + " " * 25 + "*")
    print("*" * 77)
    print("Please enter a number related to the following options to continue:")
    print("-" * 77)
    print("{:^77}".format("Options of " + menu_name + " Menu"))
    print("-" * 77)
    
def menu_room():
    while True:
        print_header("Room")
        print("1. List Rooms")
        print("2. check availability")
        print("3. Back to Main Menu\n\n")               
        choice = input("Enter your choice: ")
        if choice == "1":
            rooms = inn_room.Room.list_rooms()
            input("\nPress Enter to continue...")                       
        elif choice == "2":
            room_type = input("Rooms type: \n\nS: Standard\nP: Premium\nO: Ocean View\nE: Economy\n\nEnter room type: ")
            availability = inn_room.Room.check_availability(room_type)
            print(f"Availability of {room_type} rooms: {availability}")
            input("\nPress Enter to continue...")
        elif choice == "3":
            break               
        else:
            print("Invalid choice. Please try again.")
            
def menu_reservation():
    while True:
        print_header("Reservation")
        print("1. Check-in")
        print("2. Chek-out")
        print("3. Delete Reservation")
        print("4. List Reservations")
        print("5. Find Reservations")
        print("6. Get total cost of reservation")
        print("7. Back to Main Menu\n\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            #find the existing reservation
            phone_number= int(input("Enter the phone Number of the reservation you want to find: "))
            reservation = Reservation.find(phone_number)
            room_id = reservation[2]
            reservation_id = reservation[7]
            #Confirmar actualizar la disponibilidad de la habitacion
            print("Do you want confirm your check in? (Y/N)")
            confirm = input("Enter your choice: ")
            if confirm.lower() == "y":
                Room.decrease_availability(room_id)
                Reservation.check_in(reservation_id)
            else:
                print("Check in canceled")
                
        elif choice == "2":
            # Get user input for phone number
            phone_number = int(input("Please give your phone number:  "))
            reservation = Reservation.find(phone_number)
            room_id = reservation[2]
            checkout = reservation[6]
            reservation_id = reservation[7]  
            if checkout == 0:
                print("Customer has not checked in yet")
                print("Do you want to check in? (Y/N)")
                confirm = input("Enter your choice: ")
                if confirm.lower() == "y":
                    Room.increase_availability(room_id)
                    Reservation.check_out(reservation_id)         
            else:
                print ("Customer with phone number: has already checked out")
            
        elif choice == "3":
            reservation_id = int(input("Enter the ID of the reservation you want to delete: "))
            reservationDelete = inn_reservation.Reservation.delete_reservation_by_id(reservation_id)
        elif choice == "4":
            reservations = inn_reservation.Reservation.list_reservations()       
        elif choice == "5":
            phone_number= int(input("Enter the phone Number of the reservation you want to find: "))
            reservation = inn_reservation.Reservation.find(phone_number)  
            input("\nPress Enter to continue...")              
        elif choice == "6":
            phone_number= int(input("Enter the phone Number of the reservation you want to find: "))
            reservation = inn_reservation.Reservation.find(phone_number)
            num_days = reservation[3]
            cost_room = reservation[4]    
            print(f"Cost of Room: {cost_room}")
            print(f"Number of days: {num_days}")
            print(f"Total cost of reservation: {num_days * cost_room}")        
            input("\nPress Enter to continue...")
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main_menu()


