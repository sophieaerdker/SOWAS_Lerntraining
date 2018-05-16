import numpy as np
import matplotlib.pyplot as plt

#create polynom:

x = np.arange(-10,10)
print x
print x[0]
a = 1
b = 2
c = 3
d = 0
signal = np.empty_like(x)

for i in range(len(x)):
	j = x[i]
	signal[i] = a*j**3 + b*j**2 + c*j + d

noise = np.random.normal(0, 50, signal.shape)
y = noise + signal

plt.plot(x,y, 'o', label = "noise")
plt.plot(x, signal, 'g', label = "defined function")

z = np.polyfit(x, y, 3)
p = np.poly1d(z)
xp = np.linspace(-10,10,100)

plt.plot(xp,p(xp), 'r', label = "fit")

plt.legend()

plt.show()
