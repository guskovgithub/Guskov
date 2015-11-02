
from fractions import Fraction as fr
def q(i):
    a=fr(4,1)
    b=fr(425,100)
    for j in range(i):
        c=fr(108,1)-(fr(815,1)-fr(1500,1)/a)/b
        a,b=b,c
    a=a.limit_denominator()
    print('предел последовательности', a)
q(30)
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(1,110.01,0.1)
plt.plot(x,x**3-108*x**2+815*x-1500)
plt.grid(True)
plt.title('три корня x=5 x=3 x=100')

plt.show()
