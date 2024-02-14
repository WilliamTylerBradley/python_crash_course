guests = ['Pythagoras', 'Archimedes', 'Gauss', 'Hypatia']
print(f"{guests[0]}, you're invited to dinner")
print(f"{guests[1]}, you're invited to dinner")
print(f"{guests[2]}, you're invited to dinner")
print(f"{guests[3]}, you're invited to dinner")

print(f"{guests[1]} can't make it")

guests[1] = 'Noether'
print(f"{guests[0]}, you're invited to dinner")
print(f"{guests[1]}, you're invited to dinner")
print(f"{guests[2]}, you're invited to dinner")
print(f"{guests[3]}, you're invited to dinner")

print("I found a bigger table")

guests.insert(0, 'Turing')
guests.insert(2, 'Euclid')
guests.append('Newton')

print(f"{guests[0]}, you're invited to dinner")
print(f"{guests[1]}, you're invited to dinner")
print(f"{guests[2]}, you're invited to dinner")
print(f"{guests[3]}, you're invited to dinner")
print(f"{guests[4]}, you're invited to dinner")
print(f"{guests[5]}, you're invited to dinner")
print(f"{guests[6]}, you're invited to dinner")