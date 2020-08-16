animals = ["cat", "dog", "cheetah", "rhino"]

print(sorted(animals))
# print(animals)

print(sorted(animals, reverse=True))
# print(animals)

animals = [
    {'type': 'cat', 'name': 'Steph', 'age': 8},
    {'type': 'rhino', 'name': 'Devon', 'age': 3},
    {'type': 'dog', 'name': 'Stu', 'age': 5}
]

# print(sorted(animals))
print(sorted(animals, key=lambda animal: animal['age']))
print(sorted(animals, key=lambda animal: animal['age'], reverse=True))

# Oldest Animal
print(sorted(animals, key=lambda animal: animal['age'], reverse=True)[0])
