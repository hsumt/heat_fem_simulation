import numpy as np
N = 50 #points for the FDM
L = 100 #rod length in inches
h = L/(N+1) # spacing


temps = np.zeros(N+2)

temps[:] = 25 + (np.random.random() *10) 
temps[N//2] = 65