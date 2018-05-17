import numpy as np
import matplotlib.pyplot as plt

# 2D numpy array with 4 points:
data = np.array([[1.,2.4], [3.,4.1], [2.,3.5], [4., 5.8]], np.float32)

x = data[:,0]
y = data[:,1]

# fit 1. order polynomial:
z = np.polyfit(x, y, 1)  #returns fit parameter a,b
p = np.poly1d(z) # creates fit fuction with fit parameters

xp = np.linspace(0,5,20) #x coordinates to plot fit

plt.plot(x,y, 'o', label = "Points")
plt.plot(xp,p(xp), label = "Fit: %.2f x + %.2f" %(z[0], z[1]))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
