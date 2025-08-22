import numpy as np
import matplotlib.pyplot as plt
N = 50 #points for the FDM
L = 100 #rod length in inches
h = L/(N+1) # spacing
alpha = 0.1 
dt = 5
r = (alpha*dt)/(h**2)


temps = np.zeros(N+2)

temps[:] = 25 + (np.random.random() *10) 
temps[N//2] = 65

new_temps = np.copy(temps)
for i in range(1, N+1):
    new_temps[i] = temps[i] + r *(temps[i-1] - 2*temps[i] + temps[i+1])
temps = new_temps

plt.plot(temps)
plt.show()