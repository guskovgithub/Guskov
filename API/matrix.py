class Matrix:
    def __init__(self, m,n = None):
       if type(m) == list and n == None:
            
            self.mat = m
            self.m=len(m)
            self.n=len(m[0])
       elif  type(m) == int  and  m > 0:
           if  type(n) == int  and n > 0:
              self.m=m
              self.n=n
              mat=[[0]*self.n for i in range(self.m) ] 
              self.mat=mat 
           elif n == None: 
              self.m=m
              mat=[0]*self.m
              self.mat=mat
           else:
                raise ValueError
       else: 
              raise ValueError
                
            
    def get_m(self):
        return self.m  
    def get_n(self):
        return self.n           
    def get_size(self):
        return self.m, self.n   
    def get(self,i,j):
        return self.mat[i][j]     
    def set(self,i,j,arg):
        self.mat[i][j]=arg 
        #сложение матриц  
    def __add__(self,other):
        m=self.m
        n=self.n
        c1=[[0]*self.n for i in range(self.m)]
        for i in range(self.m):
           for  j in range(self.n):
              c1[i][j] = self.mat[i][j] + other.mat[i][j]
              c=Matrix(m, n)
              c.mat=c1
              
        return c 
        #сравнение матриц    
    def __eq__(self, other):
      if  self.m == other.m and self.n == other.n:
          if self.mat == other.mat:
              return True 
          else:
              return False
      else: 
          raise RuntimeError          
           #вычитание 
    def __sub__(self, other):
        m=self.m
        n=self.n
        c1=[[0]*self.n for i in range(self.m)]
        for i in range(self.m):
           for  j in range(self.n):
              c1[i][j] = self.mat[i][j] - other.mat[i][j]
              c=Matrix(m, n)
              c.mat=c1
        return c 
        #умножение
    def __mul__(self, other):
        m=self.m
        n=self.n
        
        if type(other) == int or type(other) == float:
           _c=[[0]*self.n for i in range(self.m)]
           for i in range(self.m):
                for  j in range(self.n):
                 _c[i][j] = self.mat[i][j] * other
                 c=Matrix(m, n)
                 c.mat=_c
           return c
           
        if (self.n == other.m):
                     
              _c=[[0]*other.n for i in range(self.m)]
              for i in range(self.m):
                   for  j in range(other.n):
                       for k in range(self.n):
                           _c[i][j] +=self.mat[i][k] * other.mat[k][j]
                           
              c=Matrix(self.m, other.n)
              c.mat = _c             
              return c    
               
        else:
           raise RuntimeError            
                        
        
        #деление
        
    def __truediv__(self, other):
        m=self.m
        n=self.n
        if type(other) == int or type(other) == float:
           c1=[[0]*self.n for i in range(self.m)]
           for i in range(self.m):
                for  j in range(self.n):
                 c1[i][j] = self.mat[i][j] / other
                 c=Matrix(m, n)
                 c.mat=c1
              
           return c         
  
  #вычсление определителя
    def little_determinant(self):
          
          
          if self.m == self.n == 2:
            
             return self.mat[0][0]*self.mat[1][1]-self.mat[1][0]*self.mat[0][1]
             
    def  determinant(self):
        
        
        if  (self.m == self.n == 3):
            det=0
            
            for i in range(self.n):
                   _c=Matrix(2,2)
                   #создаем матрицу 2 на 2 
                   for j in range(2):
                       for k in range(2):
                           if i == 0:
                                ('i =0'); _c.mat[j][k] = self.mat[j+1][k+1]  
                                (_c.mat)               
                           if i == 1:
                                if k == 0:
                                   ('i =1'); _c.mat[j][k] = self.mat[j+1][k+2]
                                   (_c.mat)     
                                if k == 1:
                                   ('i =1');  _c.mat[j][k] = self.mat[j+1][k-1]
                                      
                           if i == 2:             
                                  _c.mat[j][k] = self.mat[j+1][k]
                                              
                   det += self.mat[0][i] * _c.little_determinant()     
                    
            return det     
        elif  (self.m == self.n == 2):
             det =  self.little_determinant() 
             return det 
        else:
            raise RuntimeError  
        
    def invert(self):
       _c = Matrix(2,2)      
       for i in range(2):
          for j in range(2): 
               if (i==0 and j ==1) or (i==1 and j ==0):
                   _c.mat[i][j] = self.mat[i][j]*(-1)
               else:             
                   _c.mat[i][j] = self.mat[i][j]
                  
       return _c * (1/self.determinant()) 
    
    def transpose(self):
         x = self.n; y = self.m
         c1=[[0]*y for i in range(x)]
         for i in range(x):
            for j in range(y):
                c1[i][j] = self.mat[j][i] 
         c = Matrix(x,y)
         c.mat = c1
         return c         
        
                
