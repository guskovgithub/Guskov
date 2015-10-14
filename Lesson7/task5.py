
import numpy as np
import matplotlib.pyplot as plt
import math

x=np.arange(-20,20,0.01)
s=input()

plt.xkcd(0.6)
plt.plot(x,eval(s))
plt.axis([-20,20,-20,20])
plt.grid(True)
plt.show()
