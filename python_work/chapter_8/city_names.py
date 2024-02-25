def city_country(city, country):
    """Formats a city and country"""
    return f'{city.title()}, {country.title()}'

pair_1 = city_country('Atlanta', 'USA')
print(pair_1)
pair_2 = city_country('London', 'UK')
print(pair_2)
pair_3 = city_country('New York', 'USA')
print(pair_3)
