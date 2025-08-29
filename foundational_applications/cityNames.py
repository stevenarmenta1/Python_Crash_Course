def city_country(city, country):
    """returns a dictionary of info of city and country fully formatted"""
    location = f"{city}, {country}"
    return location.title()
    

place = city_country('San Bernardino', 'United States of America')
print(place)
place = city_country('Mexico City', 'Mexico')
print(place)
place = city_country('Rome', 'Italy')
print(place)