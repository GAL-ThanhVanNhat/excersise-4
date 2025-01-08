class PartyAnimal : 
    def __init__(self, name, x = 0) :
        self.x = x
        self.name = name
        print(f"I am constructed with {name}")
        
    def party(self) :
        self.x = self.x + 1
        print("So far",self.x, self.name)
    
    def __del__(self):
        print('I am destructed', self.x)
        

class PartyMonster(PartyAnimal):
    point =0
    def touchdown(self):
        self.point += 7
        self.party()
        print(self.name, " points" ,self.point)

an = PartyAnimal("hê hê")
an.party()
an.party()
an.party()
print("----")


an = PartyMonster("hê hê he")
an.party()
an.party()
an.party()