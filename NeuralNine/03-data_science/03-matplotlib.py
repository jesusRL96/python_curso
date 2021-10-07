import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,3*np.pi,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y1,'r--')
plt.plot(x,y2,'go')
plt.show()