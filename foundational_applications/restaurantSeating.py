numInParty = input(f"Hello, please enter how many people are in your dinner group: ")
numInParty = int(numInParty)

if numInParty > 8:
    print(f'You will have to wait for a table.')
else: 
    print(f'Your table is ready')