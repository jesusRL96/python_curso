# None recursive
n = 7 
fact = 1
while n > 0:
    fact *= n
    n -= 1

print(fact)
# recursive
def factorial(n):
    if n < 1:
        return 1
    else:
        number = n * factorial(n-1)
        return number
print(factorial(7))
# ============= fibonacci =====
# iterate
def fibonacci(n):
    a,b = 0, 1
    for x in range(n):
        a,b = b, a+b
    return a
print("Fibonacci")

# recursive
def fibonacci_2(n):
    if n <= 1:
        return n
    else:
        return (fibonacci_2(n-1) + fibonacci_2(n-2))

print(fibonacci(35))
print(fibonacci_2(35))