sandwhich_orders = ['pastrami', 'tuna', 'pastrami', 'cold cut', 'blt', 'pastrami']
finished_sandwhiches= []

print(sandwhich_orders)
print("\nWe are out of Pastrami for the day.\n")

while 'pastrami' in sandwhich_orders:
    sandwhich_orders.remove('pastrami')

while sandwhich_orders:
    current_sandwhich = sandwhich_orders.pop()

    print(f"I made you a {current_sandwhich.title()} sandwhich.")
    finished_sandwhiches.append(current_sandwhich)

print("\nThe following sandwhiches have been made:")
for finished_sandwhich in finished_sandwhiches:
    print(finished_sandwhich.title())
