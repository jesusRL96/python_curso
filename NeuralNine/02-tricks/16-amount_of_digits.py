import math
number = -99999999999999999997


digit_amount = len(str(number)) if number >= 0 else len(str(number)) - 1
print(digit_amount)
# without casting to string
if number > 0:
    print(math.ceil(math.log10(number)))   
elif number < 0:
    print(math.ceil(math.log10(-number))) 
else:
    print(1)

# 
counter = 1
while abs(number) >= (10 ** counter):
    counter += 1
print(counter)