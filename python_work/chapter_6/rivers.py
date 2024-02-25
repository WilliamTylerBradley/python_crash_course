rivers = {'nile':'egypt',
    'mississippi':'usa',
    'amazon':'brazil',
    }

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}')

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)