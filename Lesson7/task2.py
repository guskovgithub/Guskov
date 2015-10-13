import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.1)
plt.plot(x, x*x-6-x, x, [0 for i in x])
plt.show()
def func(x):
   return x*x-6-x


