def make_car(make, model, **details):
    """Creates a dictionary of car information"""
    details['make'] = make
    details['model'] = model

    return details

car = make_car('subaru', 'outback', 
               color='blue', 
               tow_package=True)

print(car)