dic1 = {'a':1, 'b': 2}
dic2 = {'c':3, 'd': 4}
# UPDATE (you can't keep their values their and save that in a third dictionary)
# dic1.update(dic2)
# print(dic1)
dic3 = {**dic1, **dic2}
print(dic3)

# only for python 3.9

dic4 = dic1 | dic2
dic5 = dic1 |= dic2
print(dic4)
print(dic5)