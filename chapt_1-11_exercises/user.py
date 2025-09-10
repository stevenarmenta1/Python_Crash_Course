class User:
    def __init__(self, first_name, last_name, phone_num, email, employee_id_num):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_num = phone_num
        self.email = email
        self.employee_id_num = employee_id_num
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user's first name is: {self.first_name}")
        print(f"The user's last name is: {self.last_name}")
        print(f"The user has a phone number: {self.phone_num} and email: {self.email}")
        print(f"The user has an employee ID number of: {self.employee_id_num}\n")
    def greet_user(self):
        print(f"Hi {self.first_name} {self.last_name}, I hope you are having a great day!\n")
    
    def increment_login_attemps(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges:
    def __init__(self, privileges):
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can delete user', 'can add admin users']
    
    def show_privileges(self):
        print("Admins have the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege.title()}") 
    
class Admin(User):
    def __init__(self, first_name, last_name, phone_num, email, employee_id_num):
        super().__init__(first_name, last_name, phone_num, email, employee_id_num)
        self.privileges = Privileges(self) 

'''
admin1 = Admin('Bobby', "Smith", "(123) 456-9060", 'bobby.smith@hotmail.com', '789453')
admin1.privileges.show_privileges()
'''
'''user1 = User('Tim', 'Brown', '(909) 678-3456', 'tim.brown@email.com', '49822')
user3 = User('Jennifer', 'Rodriguez', '(951) 789-4562', 'jen.rod@aol.com', '32166')'''

'''
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
'''
'''

user1.increment_login_attemps()
print(f"{user1.first_name} has a login attempt value of: {user1.login_attempts}")

user1.increment_login_attemps()
print(f"{user1.first_name} has a login attempt value of: {user1.login_attempts}")

user1.increment_login_attemps()
print(f"{user1.first_name} has a login attempt value of: {user1.login_attempts}")

user1.increment_login_attemps()
print(f"{user1.first_name} has a login attempt value of: {user1.login_attempts}")

user1.reset_login_attempts()
print(f"{user1.first_name}'s login attempt value has been reset to: {user1.login_attempts}")

'''