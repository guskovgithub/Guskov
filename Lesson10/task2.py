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
    
print('!!! КООРДИНАТЫ ЦЕНТРА МАСС !!!')
print(' кол-во точек') 
N=int(input())
max=0
sumX=0
sumY=0
Xc,Yc=0,0
for i in range(N):
    A=Point(input())
    sumX,sumY=A.x,A.y
    Xc+=sumX/N
    Yc+=sumY/N

print('Координыты центра  масс {', Xc,',',Yc,'}')


 
