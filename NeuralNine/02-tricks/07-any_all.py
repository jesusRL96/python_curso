# x = [True, True, True, False]
# print(any(x))
# print(all(x))
# 
numbers = [4, 5, 5, 12, 45, 7, 8]
numbers2 = [4, 8, 6, 10]
even = lambda x: x%2 == 0
print(any(list(map(even, numbers))))        # any in numbers are even ?
print(any(list(map(even, numbers2))))       # any in numbers2 are even ?
print(all(list(map(even, numbers))))        # all in numbers are even ?
print(all(list(map(even, numbers2))))       # all in numbers2 are even ?