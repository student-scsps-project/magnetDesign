import matplotlib.pyplot as plt
import numpy as np


Fs = 8000
f = 1
sample = 8000
#x = np.arange(0,np.pi/2,np.pi/2/8000)
#
#y = 23.5*np.cos(0.5 * np.pi * f * x / Fs)
x = np.arange(0,np.pi/4,0.01) # start,stop,step
y = np.cos(2*x)

x = x  * 180 / np.pi  

#plt.bar(0, 23.5, 0.2286, color="blue")
#plt.bar(0.466, 15.5, 0.304, color="blue")
#plt.bar(0.857, 11.1, 0.219, color="blue")
#plt.bar(1.227, 5.5, 0.108, color="blue")
#
#
#plt.bar(0, 19, 0.2286, color="blue")
#plt.bar(0.466, 13, 0.304, color="blue")
#plt.bar(0.857, 8, 0.219, color="blue")
#plt.bar(1.227, 4, 0.108, color="blue")
plt.plot(x, y,'k')

plt.grid(color='lightgrey', linestyle='-', linewidth=0.5)

plt.savefig("crap.pdf",format = "pdf")
plt.show()