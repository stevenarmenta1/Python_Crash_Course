prompt = input("Please enter your age for movie ticket price: ")
age = int(prompt)

if age < 3:
    print("Your ticket is free.")
elif age < 13:
    print("Your ticket is $10.")
else: 
    print("Your ticket is $15.")
``