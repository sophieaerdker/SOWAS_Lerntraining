import numpy as np
import matplotlib.pyplot as plt

#create signal without noise:
x = np.arange(-10,10)
a = 1
b = 2
c = 3
d = 0
signal = np.empty_like(x)

for i in range(len(x)):
	j = x[i]
	signal[i] = a*j**3 + b*j**2 + c*j + d

#create radnom noise and add it to the signal
noise = np.random.normal(0, 50, signal.shape)
y = noise + signal

#fit data (x,y) with polynomial of 3. order:
z = np.polyfit(x, y, 3)  #returns fit parameter a,b,c,d
p = np.poly1d(z) # creates fit fuction with fit parameters
xp = np.linspace(-10,10,100) #x coordinates to plot fit

#plot data,signal without noise and fit: 
plt.plot(x,y, 'o', label = "data with noise")
plt.plot(x, signal, 'g', label = "signal: %.2f x^3 + %.2f x^2 + %.2f x + %.2f" %(a,b,c,d))
plt.plot(xp,p(xp), 'r', label = "fit: %.2f x^3 + %.2f x^2 + %.2f x + %.2f" %(z[0], z[1], z[2], z[3]))
plt.title("Signal, Noise and Fit")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.show()
