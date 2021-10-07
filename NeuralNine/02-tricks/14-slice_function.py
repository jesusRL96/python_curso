numbers = [1, 5, 9, 15, 10, 22, 30, 25]
print(numbers[:3])
print(numbers[:-2])
# slice function
LASTFOUR = slice(-4, None)
FIRSTFOUR = slice(4)
EVERY_OTHER = slice(0, None, 2) # 2 is the stepsize
print(numbers[LASTFOUR])
print(numbers[FIRSTFOUR])
print(numbers[EVERY_OTHER])
# strings
string = "Hello world"
print(string[EVERY_OTHER])