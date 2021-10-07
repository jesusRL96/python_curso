import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib import style
from mpl_toolkits import mplot3d

# https://matplotlib.org/3.1.0/gallery/style_sheets/style_sheets_reference.html
style.use('Solarize_Light2')
# skills (BAR CHARTS)
python = (85,67,50,13,10,26,100)
java = (15,62,15,84,74,12,10)
networking = (15,48,52,95,27,20,13)
people = ['juan', 'jesus', 'pepe', 'ana', 'nic', 'maria', 'jorge']
index = np.arange(7)
# PIE CHART
nationalities = ['MX', 'VZ', 'USA', 'UK']
students = [60,25,56,80]
pairs = sorted(list(zip(students,nationalities)))
students, nationalities = zip(*pairs)
# print(students, nationalities)
# HISTOGRAM (height)
mu, sigma = 172, 8  # 172 average, 8 standard diviation
x = mu + sigma*np.random.randn(10000)

# PLOT 1 BAR CHART
gs = gridspec.GridSpec(2, 2)
fig = plt.figure(1)
fig.suptitle("Figure 1")
ax = plt.subplot(gs[0, 0]) # row 0, col 0
plt.grid(False)
plt.title("skills")
plt.xlabel("person")
plt.ylabel("points")
plt.bar(index,python,width=.2,label="python")
plt.bar(index+.2,java,width=.2,label="java")
plt.bar(index+.4,networking,width=.2,label="networking")
plt.xticks(index + 0.2, people)
plt.ylim(0,150)
ax.legend(loc="upper right")
# PLOT 2 PIE CHART
ax = plt.subplot(gs[0, 1]) # row 0, col 1
plt.title("Student's nationality")
explode = [0,.1,0,0]
plt.pie(students, labels=nationalities, explode=explode, autopct='%.2f%%', counterclock=False, startangle=90)
# PLOT 3 HISTOGRAM
ax = plt.subplot(gs[1, :]) # row 1, span all columns
plt.grid(True)
plt.title("height")
plt.hist(x, 1000, facecolor='blue', density=True)
plt.xlabel("heights")
plt.ylabel("percentage")
plt.text(140,.04,"mu=172, sig=8")


# SCATTERED PLOTS
x = np.random.rand(50)
y = np.random.rand(50)
fig = plt.figure()
plt.scatter(x,y,c='red',marker='^', s=100)

# 3D PLOTS
# single plot
z = np.linspace(0,30,100)
x = np.sin(z)
y = np.cos(z)
# 
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x,y,z)
# surface
def z_function(x,y):
    return np.sin(np.sqrt(x**2 + y**2))
x = np.linspace(-5,5,1000)
y = np.linspace(-5,5,1000)

X,Y = np.meshgrid(x,y)
Z = z_function(X,Y)
# 
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X,Y,Z)
# =================================
plt.show()