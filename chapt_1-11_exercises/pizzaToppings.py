prompt = "\nPlease enter a topping you would like on your pizza: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f'I will add {topping} to the pizza')