import numpy as np
import matplotlib.pyplot as plt

radIn=45
radOut=56

R = (radIn + radOut) / 2
h = 5.5


phi = 35.26 * np.pi / 180

#theta = np.arctan( h / (2 * R) )

theta = 2.037 * np.pi / 180

x1 = radIn * np.cos( phi - theta )
y1 = radIn * np.sin( phi - theta )

x2 = radOut * np.cos( phi - theta )
y2 = radOut * np.sin( phi - theta )

x3 = radOut * np.cos( phi + theta )
y3 = radOut * np.sin( phi + theta )

x4 = radIn * np.cos( phi + theta )
y4 = radIn * np.sin( phi + theta )

print(x1,y1)
print(x2,y2)
print(x3,y3)
print(x4,y4)