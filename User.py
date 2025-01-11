class User:
    login_attempt = 0
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")
        
    def increment_login_attempts(self):
        self.login_attempt += 1
        
    def reset_login_attempts(self):
        self.login_attempt = 0
        
u1 = User("Napoleon", "Bonaparte")
#u2 = User("George", "Washington")

u1.describe_user()
u1.greet_user()
u1.increment_login_attempts()
u1.increment_login_attempts()
print(f"Login attempts: {u1.login_attempt}")
u1.reset_login_attempts()
print(f"Login attempts: {u1.login_attempt}")

#u2.describe_user()
#u2.greet_user()