from decimal import Decimal
S0,x,y=int(input()),float(input()),int(input())
alpha=float((12+x)/12)
n=12*y
t=Decimal(alpha**(n-1)*S0*(1-alpha)/(1-alpha**(n-1))).quantize(Decimal('0.01') )            
print('размер аннуитетного платежа исходя из необходимости погасить кредит за', y,' лет',t) 
print('суммарную переплату относительно начальной суммы кредита', t*12-S0)

import numpy as np
import matplotlib.pyplot as plt
k = np.arange(1, n, 1)
plt.plot(k, alpha**(k-1)*S0- (1-alpha)/(1-alpha**(k-1))*t)
plt.show()


