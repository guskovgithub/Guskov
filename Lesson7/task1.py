from math import *
def func1(x):
    return log((1/exp(1/(sin(x)+1)))/(5/4+1/x**15), 1+x**2)
    
print(func1(1))
print(func1(10))
print(func1(1000))

