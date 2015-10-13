#from numpy import sin,pi
from pylab import plot,show, clf, ion, draw
from matplotlib import mlab
import math

a = [3]
b = [4]

T = mlab.frange(-20,20,0.01)
ion()
for n in range (50):
   x = [math.sin(a[0]*t + n/5) for t in T]
   y = [math.cos(b[0] * t) for t in T]
   clf()
   plot (x,y)
   draw()

close()
