active = True
while active:
    topping = input('\nWhat pizza topping do you want? ')
    if topping == 'quit':
        break
    else:
        print(f'Adding {topping} to your pizza!')