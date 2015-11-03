
f=open('input.txt')
ourWords=[]

for word in f.read().split():
   ourWords.append(word)
B={}
for elem in ourWords:
  B[(elem)]=ourWords.count(elem)
print(B)
