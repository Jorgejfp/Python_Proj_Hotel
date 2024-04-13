from pkt import inn_customer, inn_room, inn_reservation

def main_menu():
    while True:
        print("\n\nWelcome to Pacific Inn Reservation System\n\n")
        print("1. Menu Customer")
        print("2. Menu Room")
        print("3. Menu Reservation")
        print("4. Check In")
        print("5. Check Out")
        print("6. Exit\n\n")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            menu_customers()
        elif choice == "2":
            menu_room()
        elif choice == "3":
            menu_reservation()
        elif choice == "4":
            check_in()
        elif choice == "5":
            check_out()
        elif choice == "6":
            print("Are you sure you want to exit? (Y/N)")
            confirm = input("Enter your choice: ")
            if confirm.lower() == "y":
                print("Exiting...")
                break
            break
        else:
            print("Invalid choice. Please try again.")

        

#frm_customer = form customer
def menu_customers():
    while True:
        print("Customer Menu\n\n")
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
            delete_customer()
        elif choice == "4":
            customers = inn_customer.Customer.list_customers()
            for customer in customers:
                print(customer)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def menu_room():
    while True:
        print("Room Menu\n\n")
        print("1. List Rooms")
        print("2. check availability")
        print("3. Back to Main Menu\n\n")               
        choice = input("Enter your choice: ")
        if choice == "1":
            rooms = inn_room.Room.list_rooms()
            for room in rooms:
                print(room)
        elif choice == "2":
            room_type = input("Enter room type: \n\n" "S: Standard\n" "P: Premium\n" "O: Ocean View\n" "E: Economy\n\n")
            availability = inn_room.Room.check_availability(room_type)
            print(f"Availability of {room_type} rooms: {availability}")
        elif choice == "3":
            break               
        else:
            print("Invalid choice. Please try again.")
            
def menu_reservation():
    while True:
        print("Reservation Menu\n\n")
        print("1. Create Reservation")
        print("2. Update Reservation")
        print("3. Delete Reservation")
        print("4. List Reservations")
        print("5. Back to Main Menu\n\n")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_reservation()
        elif choice == "2":
            update_reservation()
        elif choice == "3":
            delete_reservation()
        elif choice == "4":
            reservations = inn_reservation.Reservation.list_reservations()
            for reservation in reservations:
                print(reservation)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()


# Rest of the code...


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

#crear menu con las opciones crear crear cliente, crear habitacion, crear reserva, check in, check out, salir
def create_customer():
    # Code to create a new customer
    pass




def check_in():
    # Code to check in a customer
    pass

def check_out():
    # Code to check out a customer
    pass

def create_customer():
    # Code to create a new customer
    first_name = input("Enter customer's first name: ")
    last_name = input("Enter customer's last name: ")
    email = input("Enter customer's email: ")
    phone_number = input("Enter customer's phone number: ")
    
    # Create a new customer object
    customer = inn_customer.Customer(first_name, last_name, email, phone_number)
    
    # Save the customer to the database
    customer.save()
    
    print("Customer created successfully!")
    pass

def update_customer():
    # Code to update an existing customer
    customer_id = input("Enter customer ID: ")
    first_name = input("Enter updated first name: ")
    last_name = input("Enter updated last name: ")
    email = input("Enter updated email: ")
    phone_number = input("Enter updated phone number: ")

    # Retrieve the customer from the database using the customer_id
    customer = inn_customer.Customer.get_customer_by_id(customer_id)

    # Update the customer's information
    customer.update(first_name, last_name, email, phone_number)

    print("Customer updated successfully!")
    pass

def delete_customer():
    # Code to delete a customer
    customer_id = input("Enter customer ID: ")
    # Retrieve the customer from the database using the customer_id
    customer = inn_customer.Customer.get_customer_by_id(customer_id)
    # Delete the customer from the database
    customer.delete()
    print("Customer deleted successfully!")
    pass

