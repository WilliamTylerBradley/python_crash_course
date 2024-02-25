from city_functions import format_city

def test_city_country():
    """City and country"""
    formatted_location = format_city('santiago', 'chile')
    assert formatted_location == 'Santiago, Chile'

def test_city_country_population():
    """City and country and population"""
    formatted_location = format_city('santiago', 'chile', '5000000')
    assert formatted_location == 'Santiago, Chile - population 5000000'