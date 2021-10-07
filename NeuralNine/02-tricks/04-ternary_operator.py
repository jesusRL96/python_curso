age = 23

if age >= 18:
    adult = True
    print("you're an adult")
else:
    adult = False
    print("you aren't an adult")

# ternary operator
adult = True if age >= 18 else False  # one line
print("you're an adult" if adult else "you aren't an adult")

# 
number = 10
print("this number is very large" if number > 1000 else "this number is quiet large" )