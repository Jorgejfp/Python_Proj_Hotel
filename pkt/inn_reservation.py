import mysql.connector
from pkt.connection import connectDB
from pkt.inn_room import Room



class Reservation:
    def __init__(self, room_type, customer_id, accommodation_days, checkout):
        self.id = None
        self.room_type = room_type      #int 
        self.customer_id = customer_id  
        self.accommodation_days = accommodation_days        
        self.checkout = None     
        self.totalCost = self.getTotalCost()
    
    
    #buscar el precio de la habitacion por el ID    
    def getTotalCost(self):
        room_type = self.room_type
<<<<<<< HEAD
        # buscar el precio de la habitation por el ID
        room = Room.find(room_type)
        if room:
            cost = room[2]
            totalCost= self.accommodation_days * cost      
            return totalCost
        else:
            print ("Room not found")
            return None
=======
        # Calculate the total cost based on the room type and accommodation days
        if self.room_type == "1":
            cost = 100   #buscar el precio de la habitacion por el ID
        elif self.room_type == "2":
            cost = 150
        elif self.room_type == "3":
            cost = 200        
        else:  #4
            cost = 80    
        totalCost= self.accommodation_days * cost      
        return totalCost
>>>>>>> eb2c59ff727338f70ebfd21dbbec935b90e1ef4d
    
    def changeCheckout(self):
        if self.checkout == 0:
            self.checkout = 1
        else:
            self.checkout = 0
            
    def find(phone_number):
        # Connect to the database
        connReservationDB = connectDB()
        # Create a cursor object to execute SQL queries
        cursor = None
        try:
            if connReservationDB is not None:
            
                cursor = connReservationDB.cursor()
                # Prepare the SQL query to retrieve the reservation              
                query = "SELECT first_name, last_name, room_type, totalCost, checkout FROM inn_reservation r JOIN inn_customer c ON r.customer_id = c.id WHERE c.phone_number = %s"
                # Execute the query
                cursor.execute(query, (phone_number,))
                # Fetch the result
                reservation = cursor.fetchone()
                if reservation is not None:
                    print(reservation)   
                    return reservation                
<<<<<<< HEAD
                    print("Reservation found successfully!")    
=======
                
>>>>>>> 1ae76883a26a323e06d511bba0db87c23abcb011
                else:
                    print("Reservation not found")
            else:
                print("Connection to database failed")
        except Exception as e:
            print(f"Failed to find reservation: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if connReservationDB is not None:
                connReservationDB.close()        
            
    def printReservation(self):
        print(f"Reservation ID: {self.id}")
        print(f"Room type: {self.room_type}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Accommodation days: {self.accommodation_days}")
        print(f"Cost: {self.cost}")
        print(f"Checkout: {self.checkout}")
        
    def printBilling(self):
        self.printReservation()
        print(f"Total cost: {self.getTotalCost()}")     
        
            
    def check_in(self):
        try:
            # Get user input for reservation ID
            reservation_id = input("Enter reservation ID: ")
            # Find the existing reservation
            reservation = Reservation.find(reservation_id)
            if reservation:
                # Update the checkout status of the reservation
                reservation.changeCheckout()
                print("Customer checked in successfully!")
            else:
                print("Reservation not found. Please check the reservation ID.")
        except Exception as error:
            print(f"Failed to check in customer: {error}")
            
    def check_out(self):
        
        try:
            
            # Get user input for reservation ID
            reservation_id = input("Enter reservation ID: ")
            # Find the existing reservation
            reservation = Reservation.Find(reservation_id)
            if reservation:
                # Update the check-out status of the reservation
                reservation.checkout = 1  # Suponiendo que 1 representa el estado de check-out
                print("Customer checked out successfully!")
            else:
                print("Reservation not found. Please check the reservation ID.")
        except Exception as error:
            print(f"Failed to check out customer: {error}")
                
    def create_reservation(self):
            try:
                # Get user input for reservation details
                room_type = input("Enter room type:  ")
                customer_id = input("Enter customer ID: ")
                accommodation_days = int(input("Enter accommodation days: "))
                cost = float(input("Enter cost: "))
                checkout = input("Enter checkout date: ")
                # Create a new reservation object
                reservation = Reservation(room_type, customer_id, accommodation_days, cost, checkout)
                # Save the reservation to the database
                reservation.save_dbReservation()
                print("Reservation created successfully!")
            except ValueError:
                print("Invalid input. Please enter valid values for accommodation days and cost.")
            except Exception as error:
                print(f"Failed to create reservation: {error}")
                
    def update_reservation(self):
            try:
                # Get user input for reservation details
                room_type = input("Enter room type:  ")
                customer_id = input("Enter customer ID: ")
                accommodation_days = int(input("Enter accommodation days: "))
                cost = float(input("Enter cost: "))
                checkout = input("Enter checkout date: ")
                # Create a new reservation object
                reservation = Reservation(room_type, customer_id, accommodation_days, cost, checkout)
                # Update the reservation in the database
                reservation.update_dbReservation()
                print("Reservation updated successfully!")
            except ValueError:
                print("Invalid input. Please enter valid values for accommodation days and cost.")
            except Exception as error:
                print(f"Failed to update reservation: {error}")
                
    def delete_reservation(self):
            try:
                # Get user input for reservation ID
                reservation_id = input("Enter reservation ID: ")
                # Create a new reservation object
                reservation = Reservation(None, None, None, None, None)
                reservation.id = reservation_id
                # Delete the reservation from the database
                reservation.delete_dbReservation()
                print("Reservation deleted successfully!")
            except Exception as error:
                print(f"Failed to delete reservation: {error}")
                
    #esta lista y funcionando       
    def list_reservations():
        # Connect to the database
        connReservationDB = connectDB()
        # Create a cursor object to execute SQL queries
        cursor = None
        try:
            if connReservationDB is not None:
                cursor = connReservationDB.cursor()
                # Prepare the SQL query to retrieve all reservations
                query = "SELECT * FROM inn_reservation"
                # Execute the query
                cursor.execute(query)
                # Fetch all the results
                reservations = cursor.fetchall()
                # Display the results
                for reservation in reservations:
                    print(reservation)
            else:
                print("Connection to database failed")               
        except Exception as e:
            print(f"Failed to list reservations: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if connReservationDB is not None:
                connReservationDB.close()   
    
    def save_dbReservation(self):
        # Connect to the database
        connReservationDB = None
        # Create a cursor object to execute SQL queries       
        
        try:
            if connReservationDB is not None:
                cursor = connReservationDB.cursor()
                # Prepare the SQL query to insert a new reservation
                query = "INSERT INTO inn_reservation (room_type, customer_id, accommodation_days, cost, checkout) VALUES (%s, %s, %s, %s, %s)"
                values = (self.room_type, self.customer_id, self.accommodation_days, self.cost, self.checkout)
                # Execute the query
                cursor.execute(query, values)
                # Commit the changes to the database
                connReservationDB.commit()
                
            else:
                print("Connection to database failed")
            
        except Exception as e:
            print(f"Failed to save reservation: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if connReservationDB is not None:
                connReservationDB.close()
                
            
    def update_dbReservation(self):
            try:
                # Connect to the database
                connection = connectDB()
                # Create a cursor object to execute SQL queries
                cursor = connection.cursor()
                # Prepare the SQL query to update an existing reservation
                query = "UPDATE inn_reservation SET room_type = %s, customer_id = %s, accommodation_days = %s, cost = %s, checkout = %s WHERE id = %s"
                values = (self.room_type, self.customer_id, self.accommodation_days, self.cost, self.checkout, self.id)
                # Execute the query
                cursor.execute(query, values)
                # Commit the changes to the database
                connection.commit()
                # Close the cursor and connection
                cursor.close()
                connection.close()
            except mysql.connector.Error as error:
                print(f"Failed to update reservation: {error}")
                
    def delete_dbReservation(self): 
            try:
                # Connect to the database
                connection = connectDB()
                # Create a cursor object to execute SQL queries
                cursor = connection.cursor()
                # Prepare the SQL query to delete a reservation
                query = "DELETE FROM inn_reservation WHERE id = %s"
                values = (self.id,)
                # Execute the query
                cursor.execute(query, values)
                # Commit the changes to the database
                connection.commit()
                # Close the cursor and connection
                cursor.close()
                connection.close()
            except mysql.connector.Error as error:
                print(f"Failed to delete reservation: {error}")