def city_country(city, country, population=''):
    '''returns neatly formated city, country'''
    if population:
        place = (f"{city}, {country} - {population}")
    else:
        place = (f"{city}, {country}")
        
    return place
