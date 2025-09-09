
from restaurant import Restaurant, IceCreamStand


icecream1 = IceCreamStand('Gracies', 'Mexican')
icecream1.describe_flavors()


italian_restaurant = Restaurant('Marios', 'Italian')
sushi_restaurant = Restaurant("Miguel's Sushi", "Sushi")


print(f"\nA good place to eat is {italian_restaurant.restaurant_name}.")
print(f"They make good {italian_restaurant.cuisine_type} food.")

'''
italian_restaurant.describe_restaurant()
italian_restaurant.open_restaurant()

print(f"\nFinally a great place to eat if you're feeling different is at {sushi_restaurant.restaurant_name}.")
print(f"{sushi_restaurant.restaurant_name} serves some of the best {sushi_restaurant.cuisine_type} I've ever eaten.")
sushi_restaurant.describe_restaurant()
sushi_restaurant.open_restaurant()

sushi_restaurant = Restaurant("Miguel's Sushi", "Sushi")
print(f'{sushi_restaurant.restaurant_name} has served {sushi_restaurant.number_served} people today.')

sushi_restaurant.number_served = 3
print(f'{sushi_restaurant.restaurant_name} has served {sushi_restaurant.number_served} people today.')

sushi_restaurant.set_number_served(5)
print(f'{sushi_restaurant.restaurant_name} has served {sushi_restaurant.number_served} people today.')

sushi_restaurant.increment_number_served(123)
print(f'{sushi_restaurant.restaurant_name} has served {sushi_restaurant.number_served} people today.')
'''
