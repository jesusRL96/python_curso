import numpy as np

a = np.array([
    [1,3,4,10],
    [6,5,14,25],
    [8,13,24,2],
])

print(np.cos(a))
print(np.tan(a))
print(np.sqrt(a))
print(np.log(a))
print(np.sum(a))
print(a.max(), a.min(), a.mean())
print(np.median(a), np.std(a))

# 
a = a.reshape((2,6))
print(a)
print(a.flatten())  # one dimention
# 
print(a.transpose())
print(a.flat[7])
# ===================================
a = np.array([
    [1,3,4,10],
    [6,5,14,25],
    [8,13,24,2],
])
b = np.array([
    [8,13,24,2],
    [1,3,4,10],
    [6,5,14,25],
])

c = np.concatenate((a,b))
c2 = np.stack((a,b))
c3 = np.hstack((a,b))
print(c)
print(c2)
print(c3)
# split into 2 different arrays
print(np.split(c,2))
print(np.split(c,2)[0])
# insert
a = np.array([
    [1,3,4,10],
    [6,5,14,25],
    [8,13,24,2],
    [8,13,24,2],
])
b = [999,999,999,999]
# a = np.append(a,[b],axis=0)   # insert 'b' as an arrow
a = np.insert(a,2,b,axis=1)     # insert 'b' as a column in the second possition
print(a)