responses = {}

polling_active = True

while polling_active:
    name = input('\nWhat is your name? ')
    response = input('What is your dream vacation? ')

    responses[name] = response

    repeat = input('Would you like to let another person respond? (yes/no) ')
    if repeat == 'no':
        polling_active = False

print('\n Results ')
for name, response in responses.items():
    print(f'{name}\'s dream vacation is {response}')