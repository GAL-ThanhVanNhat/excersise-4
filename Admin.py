from User import User
from Privileges import Privileges

class Admin(User):
    privileges = Privileges()
    
    def show_privileges(self):
        self.privileges.show_privileges()
        
a1 = Admin("Napoleon", "Bonaparte")
a1.show_privileges()
a1.describe_user()