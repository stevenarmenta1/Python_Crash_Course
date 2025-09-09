from user import User

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