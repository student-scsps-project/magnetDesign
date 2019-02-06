"""
A parametric fit of the critical current for varying B field.
Luke A.Dyks
"""


import numpy as np
import matplotlib.pyplot as plt


from matplotlib import rc

## for Palatino and other serif fonts use:
rc('font',**{'family':'serif','serif':['Computer Modern']})
rc('text', usetex=True)

#Fitting Parameters
alpha = 0.57
beta = 0.9
gamma = 2.32
c = 27.04 #normalisation

bc20 = 14.5#upper critical field
jcRef = 0.96 * 3000 * 10**6


tco = 9.2 #critical temp.



def jc (bMax,t): #function to calculate jc at one temp, up to Bmax

    b = np.arange(1,bMax,0.5)
    bc2 = bc20 * (1 - (t/tco)**1.7 )
    #print the value at a specific point
    #print(((jcRef * c * np.power(bf,alpha - 1))/(np.power(bc2,alpha))) * np.power(1 - (bf/bc2), beta) * np.power(1 - (t/tco)**1.7,gamma)/1e6)
    #bf = 4.2
    return ((jcRef * c * np.power(b,alpha - 1))/(np.power(bc2,alpha))) * np.power(1 - (b/bc2), beta) * np.power(1 - (t/tco)**1.7,gamma)


jc42 = jc(11,4.2)
jc19 = jc(14,1.9)

x42 = np.arange(1,11,0.5)
x19 = np.arange(1,14,0.5)

titre='criticalCurrentWithB'
plt.figure(figsize=(7.2,3.6))

plt.xlabel('B [T]')
plt.ylabel('j$_c$ [A/mm$^2$]')
plt.ylim(0,7500)

plt.grid(color='lightgrey', linestyle='-', linewidth=0.5)

plt.plot(x19,jc19/1e6,'r', label = "1.9 K")
plt.plot(x42,jc42/1e6,'b', label = "4.2 K")

plt.legend()

plt.savefig(titre + ".pdf",format = "pdf")
plt.savefig(titre + ".png", format = "png")
plt.show()