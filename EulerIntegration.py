import numpy as np
import matplotlib.pyplot as plt

t_start = 0.0
t_final = 5.0

#starting points of numerical calculation:
t = [0]
x = [1]
t_n = 0

step = 0.1

while t_n < t_final:
    x_n = x[-1] + step* x[-1] #calculate new value, with the previous value
    x.append(x_n) #store it in your data list
    t_n += step # increase the time with the step
    t.append(t_n)

#(semi-)anaytic:
t2 = np.arange(t_start, t_final, 0.001)
x2 = np.exp(t2)

#plot both in one plot:
plt.plot(t,x, 'r', label = "numeric")
plt.plot(t2, x2, 'b', label = "analytic")

plt.legend()
plt.xlabel("x")
plt.ylabel("t")
plt.title(r"Euler integration of $e^t$ with a step size of %.2f" %step)

plt.show()
