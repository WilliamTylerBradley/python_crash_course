pokemon = ['Sprigatito', 'Floragato', 'Meowscarada']
print(pokemon)

# access
print(pokemon[0])

# append
pokemon.append('Fuecoco')
pokemon.append('Skeledirge')
print(pokemon)

# insert
pokemon.insert(4, 'Crocalor')
print(pokemon)

# remove by position
del pokemon[1]
print(pokemon)

# pop
pokemon.pop(3)
print(pokemon)

# remove by value
pokemon.remove('Meowscarada')
print(pokemon)

# sort temporarily
print(sorted(pokemon))

# sort reverse temporarily
print(sorted(pokemon, reverse=True))

# sort permanently
pokemon.sort()
print(pokemon)

# sort reverse permanently
pokemon.reverse()
print(pokemon)

# length
print(len(pokemon))