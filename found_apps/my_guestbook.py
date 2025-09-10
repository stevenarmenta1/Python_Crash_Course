'''Simple program that takes guest names and writes them to guest_book.txt'''

from pathlib import Path

'''
name = input("What is your name? ")

path = Path('guest.txt')
path.write_text(name)

'''
print("Enter your name to be added to the guest list.")
print("Enter 'q' to quit.")

guest_list = ""  # initialize the guest list to start

while True:
    name = input("What is  your name? ")
    if name == 'q':
        break
    guest_list += name + "\n" # adding a new line after the name when writing the file. 

path = Path('guest_book.txt')
path.write_text(guest_list)