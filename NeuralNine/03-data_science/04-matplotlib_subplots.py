import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

x = np.arange(0,3*np.pi,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
fig1, (ax1, ax2) = plt.subplots(2)
fig1.suptitle("vertical subplot")
ax1.plot(x,y1,'g')
ax1.set_title("sin(x)")
ax2.plot(x,y2)
ax2.set_title("cos(x)")
plt.tight_layout()


fig2, axs = plt.subplots(1,2)
fig2.suptitle("horizontal subplot")
axs[0].plot(x,y1,'g')
axs[0].set_title("sin(x)")
axs[1].plot(x,y2)
axs[1].set_title("cos(x)")
plt.tight_layout()

gs = gridspec.GridSpec(2, 2)
fig3 = plt.figure()
fig3.suptitle("Figure 3")
ax = plt.subplot(gs[0, 0]) # row 0, col 0
ax.set_title("sin(x)")
plt.plot(x,y1)
ax = plt.subplot(gs[0, 1]) # row 0, col 1
ax.set_title("cos(x)")
plt.plot(x,y2)
ax = plt.subplot(gs[1, :]) # row 1, span all columns
ax.set_title("tan(x)")
plt.plot(x,y3)
plt.tight_layout()
plt.show()