fruit = 'apple'
print('Is fruit an apple? Yes')
print(fruit == 'apple')

print('Is fruit a banana? No')
print(fruit == 'banana')

pizza = 'cheese'
print('Is pizza a cheese pizza? Yes')
print(pizza == 'cheese')

print('Is pizza a pepperoni pizza? No')
print(pizza == 'pepperoni')

number_1 = 0
print('Is number_1 less than 1? Yes')
print(number_1 < 1)

print('Is number_1 less than -1? No')
print(number_1 < -1)

number_2 = 10
print('Is number_1 less than number_2? Yes')
print(number_1 < number_2)

print('Is number_1 equal to number_2? No')
print(number_1 == number_2)

number_3 = 5
print('Is number_3 greater than number_1 and less than number_2? Yes')
print((number_3 > number_1) and (number_2 > number_3))

print('Is number_3 greater than number_1 and number_2? No')
print((number_3 > number_1) and (number_3 > number_2))

state_abb = 'NC'
print('Is state NC? Yes')
print(state_abb == 'NC')

print('Is state not SC? Yes')
print(state_abb != 'SC')

print('Is state nc? Yes')
print(state_abb.lower() == 'nc')

number_1 = 0
number_2 = 1
print('Is number_1 equal to number_2? No')
print(number_1 == number_2)

print('Is number_1 not equal to number_2? Yes')
print(number_1 != number_2)

print('Is number_1 greater than number_2? No')
print(number_1 > number_2)

print('Is number_1 less than number_2? Yes')
print(number_1 < number_2)

print('Is number_1 greater than or equal to number_2? No')
print(number_1 >= number_2)

print('Is number_1 less than or equal to number_2? Yes')
print(number_1 <= number_2)

animals = ['cat', 'dog', 'rabbit']

print('Is dog an animal? Yes')
print('dog' in animals)

print('Is rock an animal? No')
print('rock' in animals)