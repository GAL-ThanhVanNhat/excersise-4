from Restaurant import Restaurant

DEFAULT_FLAVOR = ["Vanilla", "Chocolate", "Strawberry", "Mint"]

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavors = DEFAULT_FLAVOR):
        super().__init__(name, cuisine_type)
        self.flavors = flavors
        
    def show_flavors(self):
        print("The flavors are:")
        for flavor in self.flavors:
            print(f"\t{flavor}")
            
ics = IceCreamStand("Hash Robbins", "Ice Cream")
ics.describe_restaurant()
ics.show_flavors()
ics.open_restaurant()