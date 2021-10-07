import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib import style

# https://matplotlib.org/3.1.0/gallery/style_sheets/style_sheets_reference.html
# style.use('ggplot')
# style.use('fivethirtyeight')
style.use('dark_background')

x = np.arange(0,2*np.pi,0.01)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
# fig1
gs = gridspec.GridSpec(2, 2)
fig = plt.figure(1)
fig.suptitle("Figure 1")
ax = plt.subplot(gs[0, 0]) # row 0, col 0
ax.set_title("sin(x)")
ax.set_xlabel("time")
ax.set_ylabel("A")
plt.plot(x,y1)
ax = plt.subplot(gs[0, 1]) # row 0, col 1
ax.set_title("cos(x)")
plt.plot(x,y2)
ax = plt.subplot(gs[1, :]) # row 1, span all columns
ax.set_title("tan(x)")
plt.plot(x,y3)
# plt.show()

style.use('default')
style.use('Solarize_Light2')
fig2 = plt.figure(2)
plt.title("Figure 2")
plt.xlabel("time")
plt.ylabel("A")
plt.plot(x,y1, label="sin()")
plt.plot(x,y2, label="cos()")
plt.legend(loc="upper right")
plt.show()