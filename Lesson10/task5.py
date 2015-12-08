class Point:
    def __init__(self, descr):
        self.x, self.y = [float(i) for i in descr.split(',')]
    def new(x, y):
        if not (x.__class__==y.__class__==float): raise ValueError('Неправильный тип данных ')
        return Point(str(x)+','+str(y))
    def __str__(self):
        return '({}; {})'.format(self.x, self.y)
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
    def __ne__(self, other):
        return not self==other
    def __add__(self, other):
        return Point.new(self.x+other.x, self.y+other.y)
    def __radd__(self, other):
        return Point.new(self.x+other.x, self.y+other.y)
    def __neg__(self):
        return Point.new(-self.x, -self.y)
    def __sub__(self, other):
        return Point.new(self.x-other.x, self.y-other.y)
    def __rsub__(self, other):
        print(self, other)
        return Point.new(other.x-self.x, other.y-self.y)
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5
 
def plosh(a, b, c):    # ФОРМУЛА ГЕРОНА 
        return ((abs(a-b)+abs(b-c)+abs(a-c))*(abs(a-b)+abs(b-c)-abs(a-c))*(abs(a-b)+abs(a-c)-abs(b-c))*(abs(b-c)+abs(a-c)-abs(a-b)))**0.5/4
print('!!!  НАИБОЛЬШАЯ ПЛОЩАДЬ   !!!')
print(' кол-во точек')
n=int(input())
p=[Point(input()) for i in range(n)]
S=0
a,b,c=p[:3]
for vector1 in p:
    for vector2 in p:
        for vector3 in p:
            if plosh(vector1,vector2,vector3) > S:
                S = plosh(vector1,vector2,vector3)
                a,b,c=vector1,vector2,vector3
            
print(' наибольшая площадь ',S)
