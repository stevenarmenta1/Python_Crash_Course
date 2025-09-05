num = input("Greetings, please enter a number: ")
num = int(num)

if num % 10 == 0:
    print(f'Congrats! Your number {num} is a multiple of 10.')
else:
    print(f'Your number {num} is not a multiple of 10.')