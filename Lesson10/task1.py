class Point:
    def __init__(self, x = 0 , y =  0 ):
        self.x=x
        self.y=y
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
                return ((self.x)**2 + (self.y)**2)**0.5 
