
from admin_privileges import Admin

admin1 = Admin('Bobby', "Smith", "(123) 456-9060", 'bobby.smith@hotmail.com', '789453')
admin1.privileges.show_privileges()

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