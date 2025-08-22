import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
N = 50 #points for the FDM
L = 100 #rod length in inches
h = L/(N+1) # spacing
alpha = 0.1 
dt = 5
r = (alpha*dt)/(h**2)


temps = np.zeros(N+2)

temps[:] = 25 + (np.random.random() *10) 
temps[N//2] = 65

fig, ax = plt.subplots()
line, = ax.plot(temps)


def frame_update(frame):
    global temps
    new_temps = np.copy(temps)
    for i in range(1, N+1):
        new_temps[i] = temps[i] + r *(temps[i-1] - 2*temps[i] + temps[i+1])
        #Note to self: New temperature at i in the interior point range is the old temperature from before + some fraction of the difference between the neighbors. r is just the thermal diffusion controller
    temps = new_temps
    line.set_ydata(temps)
    return line,

    


#plt.plot(temps)
anim = FuncAnimation(fig, frame_update, frames=100, interval=50, blit=True)
plt.show()