numbers = [1, 5, 7, 12, 5, 10, 4, 2]

new_list = []
for number in numbers:
    if number % 2 == 0:
        new_list.append(number)

print(new_list)
# Using list comprehension
new_list_C = [x for x in numbers if x%2 == 0]
print(new_list_C)
# 
powers_of_two = [2 ** x for x in numbers]
print(powers_of_two)
# 
words = ['aUtO', 'cAR', 'AnGer', 'fox', 'PEoplE']
words = [word.upper() if word.startswith(('a', 'A')) else word.lower() for word in words ]
print(words)