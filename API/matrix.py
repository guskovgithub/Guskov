class Matrix:
    def __init__(self, m,n = None):
       if  type(m) == int  and  m > 0:
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
    def __add__(self,other):
        c=[[0]*self.n for i in range(self.m)]
        for i in range(self.m):
           for  j in range(self.n):
              c[i][j] = self.mat[i][j] + other.mat[i][j]
        return c     
   
              
               
  
                 
