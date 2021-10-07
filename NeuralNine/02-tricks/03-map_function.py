numbers = [14,5,6,7,4,8,15]

def square(x):
    return x*x
# new_list = []
# for x in numbers:
#     new_list.append(square(x))
new_list = [square(x) for x in numbers]
new_list2 = map(square, numbers)
print(new_list)
print(list(new_list2))
