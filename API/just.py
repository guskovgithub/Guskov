from matrix import *
a = Matrix(3, 2)
a.set(0, 0, -1)
a.set(0, 1, -2)
a.set(1, 0, -3)
a.set(1, 1, -4)
a.set(2, 0, -5)
a.set(2, 1, -6)

b = Matrix(3, 2)

b.set(0, 0, 4)
b.set(0, 1, 6)
b.set(1, 0, 1)
b.set(1, 1, 5)
b.set(2, 0, 87)
b.set(2, 1, 3)

        
c= a+ b         
print(c)
