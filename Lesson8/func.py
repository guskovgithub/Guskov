a=[4,4.25]
x0=float(4)
x1=float(4.25)

def func(x0,x1):
    answer=float(108-(815-1500/x0)/x1)
    return answer

flag=2
n=int(input())
while flag!=n+1:
   a.append(func(x0,x1))
   x0,x1=x1,func(x0,x1)
   flag+=1
   
print(a)
print( n, 'член последовательности', x1)
