my_names = ['jesus', 'juan', 'ana', 'pepe']

counter = 0
for name in my_names:
    print(f"{counter} - {name}")
    counter += 1
# Enumerate
for index, name in enumerate(my_names):
    print(f"{index} : {name}")

print(list(enumerate(my_names)))
print(dict(enumerate(my_names)))