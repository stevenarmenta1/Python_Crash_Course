def print_modules(unprinted_designs, completed_modules):
    """
    Simulate printing each design, until none are left. 
    Move each design to completed_modules after printing. 
    """
    while unprinted_designs: 
        current_design = unprinted_designs.pop()
        print(f'Printing model: {current_design}')
        completed_modules.append(current_design)

def show_complted_modules(completed_modules):
    """
    Show all the modules that were printed.
    """
    print("\nThe following models have been printed:")
    for completed_model in completed_modules: 
        print(completed_model)

    