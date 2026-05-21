#Car rental system
#parent class for all the classes
class vehicle():
    #Constructor method
    def __init__(self, id, make, model):
        self.id=id
        self.make=make
        self.model=model
    
    #Getters (To display vehicle information)
    def get_vehicleinfo(self):
        print(f"Vehicle Id : {self.id}")
        print(f"Make : {self.make}")
        print(f"model: {self.model}")

#Inheritance (class Car inherits from vehicle)
class Car(vehicle):
    #Constructor method
    def __init__(self,id, make, model, rent):
        #Calling parent class
        super().__init__(id, make, model)
        
        self._rent= rent
        self._available= True
    
    #Function to get daily rent price    
    def get_rent(self):
        return self._rent
    
    #Function to check availability status of a car    
    def is_available(self):
        return self._available
        
    #Rent a car if available
    def rent_car(self):
        if self._available:
            self._available= False
            print(f"{self.make} {self.model} has been rented successfully")
        else:
            print("Car is already rented")
    
    #Return a rented car    
    def return_car(self):
        self._available = True
        print(f"{self.make} {self.model} returned successfully")
        
    #To display all the cars information 
    def display_carinfo(self):
        self.get_vehicleinfo()
        
        print(f"Rent : £{self._rent} per day")
        
        if self._available:
            print("Car is available to rent")
        else:
            print("Car not available")
        
        print()

#New class customer to store customer information
class Customer:
    #Constructor method
    def __init__(self, cid, name, phone):
        self._cid=cid
        self._name=name
        self._phone=phone
    
    #To get Customer id   
    def get_cid(self):
        return self._cid
    
    #To get customer name    
    def get_name(self):
        return self._name
    
    #To get customer phone number    
    def get_phone(self):
        return self._phone
        
    #Function to display the customer's details
    def display_customerinfo(self):
        print(f"Customer ID : {self._cid}")
        print(f"Customer Name : {self._name}")
        print(f"Customer Phone Number : {self._phone}")
        print()
        
#Rental class to store rental information
class Rental:
    #Constructor method
    def __init__(self, rental_id, customer, car, rental_days):
        self.rental_id= rental_id
        self.customer= customer
        self.car= car
        self.rental_days= rental_days
    
    #To get the total cost of renting    
    def totalcost(self):
        return self.car.get_rent() * self.rental_days
    
    #To display the rental information  
    def display_rentalinfo(self):
        print()
        print("**********Rental Details**********")
        print(f"Rental Id : {self.rental_id}")
        print(f"Customer : {self.customer.get_name()}")
        print(f"Car : {self.car.make} {self.car.model}")
        print(f"Days : {self.rental_days}")
        print(f"Total Cost : £{self.totalcost()}")
        print()

"""Empty lists to store information of cars, customers and rentals"""
cars= []
customers= []
rentals= []

#adding sample cars for renting by creating car objects
car1=Car(101,"Toyota","Corolla",50)
car2=Car(102,"Toyota","Auris",70)
car3=Car(103,"BMW","I5",150)
car4=Car(104,"Audi","A8",100)
car5=Car(105,"Hyundai","Elantra",90)

#using append keyword to insert the data into the list
cars.append(car1)
cars.append(car2)
cars.append(car3)
cars.append(car4)
cars.append(car5)

#function to display all the cars
def view_cars():
    print("###Available Cars###")
    for car in cars:
        car.display_carinfo()

#function to add customers   
def add_customer():
    #getting the user input
    customer_id=input("Enter customer id: ")
    name=input("Enter customer name: ")
    phone=input("Enter customer's phone number: ")
    
    customer=Customer(customer_id, name, phone)
    
    customers.append(customer)
    
    print("Customer added successfully")
    
#Function to view customer list    
def view_customers():
    if len(customers)==0:
        print("No customers found")
    else:
        print()
        print("Customer List")
        
        for customer in customers:
            customer.display_customerinfo()


#Function to rent a car
def rent_car():
    #getting the user input 
    car_id=int(input("Enter Car ID: "))
    customer_id=input("Enter Customer ID: ")
    days=int(input("Enter Rental Days: "))

    #Search for selected car cars
    for car in cars:
        
        #Check if the car id matches
        if car.id == car_id:

            #Check for the availability of the car
            if car.is_available():

                #check for customer
                for customer in customers:

                    #check if customer id matches
                    if customer.get_cid() == customer_id:
                        
                        #Create rental object
                        rental = Rental(len(rentals) + 1,customer,car,days)

                        rentals.append(rental)

                        car.rent_car()

                        print("Car rented successfully")

                        return
                
                #If customer is not found
                print("Customer not found")
                return

            else:
                print("Car not available")
                return

    print("Car not found")

#Function to return a rented car
def return_car():
    #getting user input for the car id which is to be returned
    car_id=int(input("Enter Car ID to return "))
    
    #Search for car
    for car in cars:
         
        #match the car id
        if car.id == car_id:
            
            #Check if the car has already been returned or not
            if car.is_available():
                print("Car already returned.")
            else:
                car.return_car()

            return

    print("Car not found.")

#Function to view rentals
def view_rentals():
    #To check if any car has been rented or not
    if len(rentals) == 0:
        print("No rentals found.")
        return
    #Display all the rentals
    for rental in rentals:
        rental.display_rentalinfo()

#Main Loop    
while True:
    print("\n")
    print("**********Car rental system**********")
    print("1. View Cars")
    print("2. Add Customer")
    print("3. View Customers")
    print("4. Rent Car")
    print("5. Return Car")
    print("6. View Rentals")
    print("7. Exit")
    
    #Getting user's choice
    choice = input("Enter your choice: ")
    
    if choice == "1":
        view_cars()
    elif choice == "2":
        add_customer()
    elif choice == "3":
        view_customers()
    elif choice == "4":
        rent_car()
    elif choice == "5":
        return_car()
    elif choice == "6":
        view_rentals()
    elif choice == "7":
        print("Thank you for using the Car Rental System.")
        break #End the loop immediately
    else:
        print("Wrong choice try again")
        print("Invalid choice. Please try again.")