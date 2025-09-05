def toppings_sandwhich(*toppings):
    print(f'\nMaking a sandwhich with your following selections: ')
    for topping in toppings:
        print(f'- {topping.title()}')
        

toppings_sandwhich('ham', 'cheese', 'bacon')
toppings_sandwhich('BACON')
toppings_sandwhich("Turkey", "Onions", "Tomatoe")