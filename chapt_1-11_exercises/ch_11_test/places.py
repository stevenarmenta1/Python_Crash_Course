from city_functions import city_country

print("Enter 'q' to quit at any time.")
while True:
    city = input("Name of city: ")
    if city == 'q':
        break
    country = input("Name of country: ")
    if country == 'q':
        break

    place = city_country(city, country)
    print(place)