sandwich_orders = ['rueben', 'pastrami', 'ham and cheese', 'pastrami', 'peanut butter and jelly', 'pastrami']
finished_sandwiches = []

print('The deli has ran out of pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'I made your {current_sandwich}')
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print(f'{sandwich} was made.')
