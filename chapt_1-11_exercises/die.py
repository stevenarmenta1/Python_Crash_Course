from random import randint

class Die:
    '''Class that is for rolling dice'''
    def __init__(self, sides=6):
        self.sides = sides 
    
    def roll_die(self):
        return randint(1, self.sides)

sides = Die()
print(sides.roll_die())

sides = Die(10)
print(sides.roll_die())

sides = Die(20)
print(sides.roll_die())