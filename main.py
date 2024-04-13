from pkt import inn_customer, inn_room, inn_reservation
from pkt.inn_customer import Customer
from pkt.inn_room import Room
from pkt.inn_reservation import Reservation
from pkt.connection import connectDB

try:
    with open("reservation_file.txt", "r") as f1:
        reservations = []

        for line in f1.readlines():
            data = line.strip().split(",")
            reservation_duration = data[5]  # Suponiendo que la duración de la reserva está en la última posición de los datos

            # Crear un nuevo objeto Customer con los datos de la línea posicion 0,1,2,3
            customer = Customer(data[0], data[1], data[2], data[3])
            
            # buscar el ID asociado al tipo de habitacion
            room_id = Room.getID(data[4])
           
            
            # y luego recuperar las claves primarias generadas automáticamente
            customer_id = customer.getCostumerId(data[3])
            
            # tenemos las claves primarias customer_id y room_id
         
            # Creamos un nuevo objeto Reservation con las claves externas correctas
            reservation = Reservation(customer_id, room_id, reservation_duration)
            reservations.append(reservation)

    # Imprimir las reservaciones
    for reservation in reservations:
        print(reservation)

except FileNotFoundError:
    print("El archivo reservation_file.txt no se ha encontrado.")
except Exception as e:
    print(f"Se produjo un error: {e}")

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

