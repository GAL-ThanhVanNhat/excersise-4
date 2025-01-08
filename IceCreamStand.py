from Restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint"]
    def show_flavors(self):
        print("The flavors are:")
        for flavor in self.flavors:
            print(f"\t{flavor}")
            
ics = IceCreamStand("Baskin Robbins", "Ice Cream")
ics.describe_restaurant()
ics.show_flavors()
ics.open_restaurant()