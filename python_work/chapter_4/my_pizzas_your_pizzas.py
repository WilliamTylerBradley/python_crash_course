pizzas = ['cheese', 'pepperoni', 'supreme']

friend_pizzas = pizzas[:]

pizzas.append('veggie')

friend_pizzas.append('meat lovers')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)