mysquare = lambda x: x ** 2
# mysum = lambda x, y: x + y
mysum = lambda *args: sum(args)

print(mysum(5,3,10,40))
print((lambda x: x ** 2)(3))
# 
numbers = [15, 6, 9, 11, 9, 16]
# def filter_function(x):
#     return x % 2 == 0
# even_numbers = filter(filter_function, numbers)
# print(list(even_numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)
# 
def my_function(num):
    return lambda x: x *num

ten_multiplier = my_function(10)    # num will take the value of 10
print(ten_multiplier(5))           # x will take the value of 5