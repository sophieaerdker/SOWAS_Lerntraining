import numpy as np
import matplotlib.pyplot as plt

#Create the plot data (lists):
x = np.arange(0.0, 2*np.pi, 0.01)
y = np.sin(x)

#The simplest plot statement without many
#configuration posibilities:
plt.plot(x,y)

plt.xlabel("x")
plt.ylabel("y")
plt.title("A function")

plt.savefig("Plot.png") #if you want to save your plot
plt.show() #to see your plot on screen
