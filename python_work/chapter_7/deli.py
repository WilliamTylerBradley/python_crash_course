sandwich_orders = ['rueben', 'ham and cheese', 'peanut butter and jelly']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'I made your {current_sandwich}')
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print(f'{sandwich} was made.')
