from city_functions import city_country

def test_city_country_format():
    '''Test that city and country names like Santiago and Chile work.'''
    place_name = city_country('Santiago', "Chile")
    assert place_name == 'Santiago, Chile'

def test_city_country_population_format():
    '''Do places like Santiago, Chile - 5000000 work?'''
    place = city_country( 'Santiago', 'Chile', population=5000000)
    assert place == 'Santiago, Chile - 5000000'