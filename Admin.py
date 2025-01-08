from User import User
from Privileges import Privileges

class Admin(User):
    privileges = Privileges()
    
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        
    def show_privileges(self):
        self.privileges.show_privileges()
        
a1 = Admin("Napoleon", "Bonaparte")
a1.show_privileges()
a1.describe_user()