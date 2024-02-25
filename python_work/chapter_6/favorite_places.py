favorite_places = {
    'Liam':['SC'],
    'Matt':['NC', 'TN'],
    'Noah':['VA', 'DC'],
}

for name, places in favorite_places.items():
    if len(places) > 1:
        print(f"{name}'s favorite places are {places}")
    else:
        print(f"{name}'s favorite place is {places}")