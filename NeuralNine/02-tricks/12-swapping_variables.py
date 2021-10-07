a = 10
b = 20
c = 30
d = 40
# temp = a
# a = b
# b = temp
a, b, c, d = d, c, b, a
print(a, b, c, d)
#  swapping using binary representation
'''
 24 = 011000
 41 = 101001
XOR = 110001    ->MASK

'''
a = 24
b = 41
a = a ^ b
b = b ^ a
a = a ^ b
print(a, b)