print("Give me two numbers and I'll add them together.")
print("Enter 'q' to quit.")

while True:
    first_num = input("\nFirst number: ")
    if first_num == 'q':
        break
    second_num = input("\nSecond number: ")
    if second_num == 'q':
        break
    try:
        first_num = int(first_num)
        second_num = int(second_num)
        answer = first_num + second_num
    except ValueError:
        print("Only numbers are accepted, thank you.")
    else: 
        print(answer)