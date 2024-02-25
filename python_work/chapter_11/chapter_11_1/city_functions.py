def format_city(city, country, population = ''):
    """Format city and country"""
    if population:
        return f'{city.title()}, {country.title()} - population {population}'
    else:
        return f'{city.title()}, {country.title()}'