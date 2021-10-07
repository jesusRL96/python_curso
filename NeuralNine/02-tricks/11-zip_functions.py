names = ["jesus", "pepe", "juan", "maria"]
ages = [23, 18, 44, 17]
# for i in range(len(names)):
#     print(f"Name: {names[i]}, age: {ages[i]}")

#  Zip
# print(list(zip(names, ages)))
for name, age in zip(names, ages):
    print(f"Name: {name}, age: {age}")

# 
sales = [500, 300, 400, 1200, 600]
costs = [200, 600, 200, 300, 400]
for sale, cost in zip(sales, costs):
    print(sale - cost)
# 
zipped = [('Mike', 50), ('jose', 20), ('pepe', 30)]
names, ages = zip(*zipped) 
print(names)
print(ages)
# 
letters = ['b', 'c', 'd', 'a']
numbers = [1, 4, 3, 2]
# it's sorted by letters and connected to the right number
data = sorted(zip(letters, numbers))
print(data)
# it's sorted by numbers and connected to the right letter
data = sorted(zip(numbers, letters))
print(data)
# both list are now independent, numbers are still sorted, and connected to the right letter 
numbers, letters = zip(*data)
print(numbers)
print(letters)
# convet in dictionary
mydict = dict(zip(numbers, letters))
print(mydict)