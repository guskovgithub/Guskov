import numpy as np
import matplotlib.pyplot as plt
import math
x=np.arange(-10,10,0.01)
def f(x):
   return np.log(  (x**2+1)*np.exp(-np.abs(x)/10) ,(1+np.tan(1/(1+np.sin(x)**2))) )
   
plt.plot(x, f(x))
#plt.plot(x, [0 for i in x])
plt.axis('equal')
plt.show()
