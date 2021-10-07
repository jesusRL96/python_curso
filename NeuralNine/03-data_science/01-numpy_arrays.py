import numpy as np
a = [1,2,3,4]
b = [5,6,7,8]


c = np.array([
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4],
])
x = []
print(c.shape)
print(a+b)
a = np.array(a)
b = np.array(b)
print(a+b)
# =======================================
a = np.zeros((3,7,5))
a = np.ones((3,7,5))
a = np.full((3,7,5), 9)
a = np.empty((1,3,5))
a = np.random.random((1,3,5))
a = np.identity(5)
print(a)
# =======================================
x = np.arange(0,100,10)     # initial, final, step
y = np.sin(x)
x = np.linspace(0,100,7)     # initial, final, number of values
y = np.sin(x)
print(x)
print(y)
# =======================================
a = np.full((2,3,5),8,dtype=float)
# print(a)
print(a.shape)
print(a.size)
print(a.ndim)
print(a.dtype)