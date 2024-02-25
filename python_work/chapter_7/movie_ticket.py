while True:
    age = input('\nWhat is your age? ')
    if age == 'quit':
        break
    else:
        if int(age) < 3:
            print(f'Ticket is free.')
        elif int(age) < 13:
            print(f'Ticket is $10.')
        else:
            print('Ticket is $15.')