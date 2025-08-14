responses = {}

poll_active = True
while poll_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to let someone else respond to the poll? (yes / no) ")
    if repeat == 'no':
        poll_active = False

print("\n--- Polling is Done ---")
for name, response in responses.items():
    print(f"{name} would like to have a dream vacation in {response.title()}.")
