import numpy as np
import matplotlib.pyplot as plt


f=open('TextForTask6.txt')
ourWords=[]
for word in f.read().split():
     ourWords.append(word)

     
def MaxLenthWord(ourWords):
     max=0
     for i in range(len(ourWords)):
           if len(ourWords[i])>max:
                max=len(ourWords[i])
     return max


w=[]
for elem in ourWords:
     w.append(int(len(elem)))


count=[0]*(MaxLenthWord(ourWords))
for j in range(1,MaxLenthWord(ourWords)+1):
      for i in range(len(w)):
             if w[i]==j:
                  count[j-1]+=1



line=[]
for i in range(1,max(w)+1):
     line.append(i)


plt.bar(line, count, align='center', alpha=0.7)
plt.xticks( line, line)
plt.ylabel('How much words')
plt.xlabel('Lenght of words')
plt.title('War and Peace Chapter I')
plt.show()                
     

f.close()
