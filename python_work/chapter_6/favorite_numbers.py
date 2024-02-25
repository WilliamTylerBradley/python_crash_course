favorite_numbers = {'Alex':5, 
    'Bill':[13], 
    'Cynthia':[3], 
    'David':[7, 14], 
    'Edward':[21],
    }

for name, numbers in favorite_numbers.items():
    print(f'{name}: {numbers}')