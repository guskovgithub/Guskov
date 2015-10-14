import matplotlib.pyplot as plt
import numpy as np
from math import pi

x=np.arange(-2,2,0.001)
w=0
b=0.5
a=5

for n in range(20):
   w+=(b**n)*np.cos((a**n)*x*pi)
   

plt.plot(x,w)
plt.show()
