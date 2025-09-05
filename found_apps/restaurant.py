class Restaurant:
    '''
    '''

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes the restaurant name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a great place that serves {self.cuisine_type} food.")
    
    def open_restaurant(self): 
        print(f"{self.restaurant_name} is now open and ready to serve!")
    
    def set_number_served(self, customers_served):
        '''sets the number of people served to a value'''
        self.number_served = customers_served
    
    def increment_number_served(self, customers_served):
        self.number_served += customers_served
    

'''
restaurant1 = Restaurant('Gracies', 'Mexican')
italian_restaurant = Restaurant('Marios', 'Italian')
sushi_restaurant = Restaurant("Miguel's Sushi", "Sushi")


print(f"My favorite place to eat is {restaurant1.restaurant_name}.")
print(f"The restaurant makes the best {restaurant1.cuisine_type} food I've ever eaten.")

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

print(f"\nAnother place that is good is {italian_restaurant.restaurant_name}.")
print(f"They make good {italian_restaurant.cuisine_type} food.")

italian_restaurant.describe_restaurant()
italian_restaurant.open_restaurant()

print(f"\nFinally a great place to eat if you're feeling different is at {sushi_restaurant.restaurant_name}.")
print(f"{sushi_restaurant.restaurant_name} serves some of the best {sushi_restaurant.cuisine_type} I've ever eaten.")
sushi_restaurant.describe_restaurant()
sushi_restaurant.open_restaurant()
'''
sushi_restaurant = Restaurant("Miguel's Sushi", "Sushi")
print(f'{sushi_restaurant.restaurant_name} has served {sushi_restaurant.number_served} people today.')

sushi_restaurant.number_served = 3
print(f'{sushi_restaurant.restaurant_name} has served {sushi_restaurant.number_served} people today.')

sushi_restaurant.set_number_served(5)
print(f'{sushi_restaurant.restaurant_name} has served {sushi_restaurant.number_served} people today.')

sushi_restaurant.increment_number_served(123)
print(f'{sushi_restaurant.restaurant_name} has served {sushi_restaurant.number_served} people today.')
