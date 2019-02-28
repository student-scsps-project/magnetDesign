"""
Plotting the load line for our quad
Luke A.Dyks
"""


import numpy as np
import matplotlib.pyplot as plt


from matplotlib import rc

## for Palatino and other serif fonts use:
rc('font',**{'family':'serif','serif':['Computer Modern']})
rc('text', usetex=True)

####READ IN CURRENT FILE
filename = "quadCurrentsThickerCoils.dat"
infile = open(filename)
dt = [("#I","f"),("grad","f"),("B","f")]
A = np.loadtxt(filename, dtype=dt)
iQuad = A["#I"]
poleTipField = A["B"]



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
    bf = 7.24
    print((36/ 2.5 ) * (np.pi * 0.825**2 / 4)*((jcRef * c * np.power(bf,alpha - 1))/(np.power(bc2,alpha))) * np.power(1 - (bf/bc2), beta) * np.power(1 - (t/tco)**1.7,gamma)/1e6)
    
    return ((jcRef * c * np.power(b,alpha - 1))/(np.power(bc2,alpha))) * np.power(1 - (b/bc2), beta) * np.power(1 - (t/tco)**1.7,gamma)


jc42 = jc(11,4.2)/1e6
jc19 = jc(14,1.9)/1e6

I42 = jc42 * (36/ 2.5 ) * (np.pi * 0.825**2 / 4)
I19 = jc19 * (36/2.5) * (np.pi * 0.825**2 / 4)



x42 = np.arange(1,11,0.5)
x19 = np.arange(1,14,0.5)

titre='quadLoadLineThickerCoils'
plt.figure(figsize=(7.2,3.6))

plt.xlabel('B [T]')
plt.ylabel('I [A]')
plt.xlim(0,10)
plt.ylim(0,25000)

plt.grid(color='lightgrey', linestyle='-', linewidth=0.5)

plt.plot(x19,I19,'r', label = "1.9 K")
plt.plot(x42,I42,'b', label = "4.2 K")
plt.plot(poleTipField,iQuad,'g', label = "B Peak Inner Coil")

plt.legend()

plt.savefig(titre + ".pdf",format = "pdf")
plt.savefig(titre + ".png", format = "png")
plt.show()