class Point:
    def __init__(self,line='0,0'):
        self.x, self.y = [float(i) for i in line.split(',')]
    def __str__(self):
         return 'x = ' + str(self.x) + ' y = ' + str(self.y)    
    def __add__(self, other):
               return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
                return Point(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
                return Point(self.x * other.x, self.y * other.y)
    def __truediv__(self, other):
                return Point(self.x / other.x, self.y / other.y)
    def __floordiv__(self, other):
                return Point(self.x // other.x, self.y // other.y)                               
    def __mod__(self, other):
                return Point(self.x % other.x, self.y % other.y)  
    def __pow__(self, other):
                return Point(self.x ** other.x, self.y ** other.y)  
    def __abs__(self):
                return (int(self.x)**2 + int(self.y)**2)**0.5
    
print('!!! НАИБОЛЕЕ УДАЛЕННАЯ ТОЧКА !!!')
print(' кол-во точек') 


N = int(input())
max = 0
x,y = 0,0
for i in range (N):
    a = Point(input())
    if abs(a) > max:
        max = abs(a)
        x = a.x
        y = a.y
print('НАИБОЛЕЕ УДАЛЕННАЯ ТОЧКА {', x,',',y,'}')
 
