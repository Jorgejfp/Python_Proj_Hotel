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
        self.totalCost = None #self.getTotalCost()
    
    
    #buscar el precio de la habitacion por el ID    
    #def getTotalCost(self):
        #Buscar el precio de la habitacion por el ID
        # try:
        #     # Connect to the database
        #     connRoomDB = connectDB()
        #     cursor = None
        #     if connRoomDB is not None:
        #         cursor = connRoomDB.cursor()
        #         # Prepare the SQL query to select the customer by ID
        #         query = "SELECT * FROM inn_rooms WHERE id = %s"
        #         cursor.execute(query, (self.customer_id))
        #         room_data = cursor.fetchone()
        #         if room_data is not None:
        #             # Create a Room Data object from the fetched data
        #             cost = Room(*room_data)
        #             return cost
        #         else:
        #             print("Room type with ID {} does not exist.".format(self))
        #     else:
        #         print("Error: Could not connect to database")
        # except Exception as e:
        #     print(f"Error when fetching customer data: {e}")
        # finally:
        #     if cursor is not None:
        #         cursor.close()
        #     if connRoomDB is not None:
        #         connRoomDB.close()
    
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
                query = "SELECT first_name, last_name, r.room_type, accommodation_days, room_price, cost, checkout, r.id FROM inn_reservation r JOIN inn_customer c ON r.customer_id = c.id JOIN inn_rooms d ON r.room_type = d.id WHERE c.phone_number = %s"
                # Execute the query
                cursor.execute(query, (phone_number,))
                # Fetch the result
                reservation = cursor.fetchone()
                if reservation is not None:
                    #print(reservation)   
                    return reservation               
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
        #actualizar el estado de check-in
        try:
            # Connect to the database
            connCheckStatus = connectDB()
            # Create a cursor object to execute SQL queries
            cursor = connCheckStatus .cursor()
            # Prepare the SQL query to update an existing reservation
            query = "UPDATE inn_reservation SET checkout = %s WHERE id = %s"
            values = (0, self)
            # Execute the query
            cursor.execute(query, values)
            # Commit the changes to the database
            connCheckStatus.commit()
            # Close the cursor and connection
            cursor.close()
            connCheckStatus.close()
        except mysql.connector.Error as error:
            print(f"Failed to update reservation: {error}")

        print("Customer checked in successfully!") 
        
    def check_out(self):
<<<<<<< HEAD
        room = Room()
        # Get user input for phone number
        phone_number = input("Please give your phone number:  ")
        # Find the existing reservation
        reservation = Reservation.find(phone_number)
        if reservation is not None:
            checkout = reservation[6]
            room_type = reservation[2]
            room.availability = room.check_availability(room_type)
            if checkout == 0:
                print("Customer has not been checked out")
            else:
                #aumenta a 1
                room.increase_availability(room_type)
                print("Customer has been checked out succefully!")
                print("Your invoice information is: \n\n Name: ", reservation[0], reservation[1], "\n Accommodation days: ", reservation[3], "\n Room Type: ", reservation[2],  "\n Total Cost: ", reservation[5])
        else:   
            print("Phone number not found. Please check phone number.")  
            
            
=======
        connReservationDB = connectDB()
        cursor = None
        try:
            if connReservationDB is not None:
                cursor = connReservationDB.cursor()
                # Prepare the SQL query to update the checkout status of a reservation
                query = "UPDATE inn_reservation SET checkout = 1, availability = availability +1  WHERE phonenumber = %s"
                values = (1,self.phonenumber,)
                cursor.execute(query, values)
                # Commit the changes to the database
                connReservationDB.commit()
                print("Customer checked out successfully!")
            else:
                print("Connection to database failed")  
        except Exception as e:
            print(f"Failed to check out customer: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if connReservationDB is not None:
                connReservationDB.close()
                
>>>>>>> 1ce5a45bbb760ce4330b36096a4e4c63eb747121
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