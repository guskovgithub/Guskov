
words=open('TextForTask3.txt','r')
stat={}
for word in words.read().split():
    word=word.replace(',','').replace('.','').replace(':','').replace('!','').replace('"','').replace('?','').replace('-','').replace(')','').replace('(','')
    word=word.lower()
    if word in stat:
          stat[word]+=1
    else:
        stat[word]=1
count=0
for key in stat:
   if stat[key] > count:
      count=stat[key]
   
   print(key, stat[key])
PopularWords=[]
for key in stat:
    if stat[key]==count:
       PopularWords.append(stat[key])
       PopularWords.append(key)
 


PopularWords=PopularWords[::-1]
print('!!! Наиболее встречаемые слова !!! :')

for i in range(0,int(len(PopularWords)/2)+1,2):
    print(PopularWords[i], end=' ')
    print(PopularWords[i+1], 'раза')




