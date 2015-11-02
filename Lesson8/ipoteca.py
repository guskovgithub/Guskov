from decimal import Decimal
print('сумма  ',' проценты в форме 0,**   '   ,  'срок(лет)  ', '(по отдельностив каждой строчке)' )
S0,x,y=int(input()),float(input()),int(input())
alpha=float((12+x)/12)
n=12*y
babloNorm=Decimal(S0*(x/12+(x/12)/((1+x/12)**(y*12)-1))).quantize(Decimal('0.01') )  #ежемесячная выплата         
bablo=S0*(x/12+(x/12)/((1+x/12)**(y*12)-1))
print('размер аннуитетного платежа исходя из необходимости погасить кредит за', y,'лет',babloNorm) 
print('суммарную переплату относительно начальной суммы кредита', babloNorm*n-S0)

#таблица
mass=[ [0] * 4 for i in range(n+1)]
ostatok=[]
ostatok.append(S0)
mass[0][0]='Выплата'
mass[0][1]='Остаток'
mass[0][2]='На %'
mass[0][3]='На сумму долга'
for i in range(1,n+1):
  ostatok.append(ostatok[i-1]*(12+x)/12-bablo)
  if babloNorm<ostatok[i-2]*(12+x)/12-bablo:
      mass[i][0]=babloNorm
      mass[i][1]=Decimal(ostatok[i-1]*(12+x)/12-bablo).quantize(Decimal('0.01') )
      mass[i][2]=Decimal(ostatok[i-1]*(x)/12).quantize(Decimal('0.01') )
      mass[i][3]=Decimal(bablo-ostatok[i-1]*(x)/12).quantize(Decimal('0.01') )
  else:
      mass[i][0]=Decimal(ostatok[i-2]*(12+x)/12-bablo).quantize(Decimal('0.01') )
      mass[i][1]= 0
      mass[i][2]=Decimal(ostatok[i-1]*(x)/12).quantize(Decimal('0.01') )
      mass[i][3]=Decimal(ostatok[i-1]-ostatok[i-1]*(x)/12).quantize(Decimal('0.01') )

ostatok.pop()


for row in mass:
    for elem in row:
        print(elem, end='    ')
    print()

import numpy as np
import matplotlib.pyplot as plt

#график остатка (в целом)
mounth=[]
for i in range(1,n+1):
   mounth.append(i) 

plt.subplot(2, 2, 1) 
plt.bar(mounth,ostatok, align='center', alpha=0.7)
plt.xticks( mounth, mounth)
plt.ylabel('Остаток')
plt.xlabel('Месяц')
plt.title('Остаток по кредиту')
plt.subplots_adjust(left=0.15)



plt.subplot(2, 2, 2)
proz=[]
for i in range(1,n+1):
   proz.append(mass[i][2])
plt.bar(mounth,proz, align='center', alpha=0.7)
plt.xticks( mounth, mounth)
plt.ylabel('На проценты')
plt.xlabel('Месяц')
plt.title('Погашение процентов')
plt.subplots_adjust(left=0.15)


plt.subplot(2, 2, 3)
basic=[]
for i in range(1,n+1):
   basic.append(mass[i][3])
plt.bar(mounth,basic, align='center', alpha=0.7)
plt.xticks( mounth, mounth)
plt.ylabel('На основную сумму')
plt.xlabel('Месяц')
plt.title('Погашение основной суммы')
plt.subplots_adjust(left=0.15)
plt.show()





