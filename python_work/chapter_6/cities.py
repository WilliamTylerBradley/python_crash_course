cities = {
    'asheville': {
        'country':'us', 
        'population':94067,
        'fact':'It’s known for a vibrant arts scene and historic architecture',
    },
    'raleigh': {
        'country':'us', 
        'population':469124,
        'fact':'Raleigh is the capital city of North Carolina',
    },
    'greensboro': {
        'country':'us', 
        'population':298263,
        'fact':'The Greensboro Science Center houses red pandas, sharks and a hands-on museum',        
    }
}

for city, information in cities.items():
    for k, v in information.items():
        print(f'{city} {k} {v}')