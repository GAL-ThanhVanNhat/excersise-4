class Restaurant: 
    def __init__(self, name, cuisine_type):
        served_number = 0
        self.name = name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"The restaurant {self.name} serves {self.cuisine_type} food.")
    def open_restaurant(self):
        print(f"{self.name} is now open.")
    def set_number_served(self, number):
        self.served_number = number
    def increment_number_served(self, number):
        self.served_number += number
    def print_server_number(self):
        print(f"The number of served customers is {self.served_number}.")   
        
#r1 = Restaurant("The Fat Radish", "American")
#r2 = Restaurant("Quán bún", "Bún bò Huế")
#r3 = Restaurant("Quán Phở", "Phở Bắc")

#r1.describe_restaurant()
#r1.open_restaurant()
#r1.set_number_served(10)
#r1.print_server_number()
#r1.increment_number_served(5)
#r1.print_server_number()

#r2.describe_restaurant()
#r2.open_restaurant()

#r3.describe_restaurant()
#r3.open_restaurant()
