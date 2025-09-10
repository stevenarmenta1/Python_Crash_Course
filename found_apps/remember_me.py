from pathlib import Path
import json

def get_stored_info(path):
    '''Get user's stored name, phone number and email if available.'''
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)
    else:
        return None

def saved_user_info(path, info):
    '''Saves user info to the file.'''
    contents = json.dumps(info, indent=4)
    path.write_text(contents)

def display_user_info():
    '''Greets the user and displays there number, and email.'''
    path = Path('user_info.json')
    info = get_stored_info(path)
    
    
    name = input(f"Is this your username? {info['name']} (y/n) ")


    if name == 'y' : 
        print(f"Welcome back {info['name']}")
        print(f"Your saved info: ")
        print(f"  -Phone: {info['phone']}")
        print(f"  -Email: {info['email']}")
    else: 
        name = input("What is your username? ")
        phone = input("What is your phone number? ")
        email = input("What is your email? ")
    
        info = {
            'name': name,
            'phone': phone,
            'email': email
        }

        saved_user_info(path, info)
        print("I will remember this info, thank you.")

display_user_info()