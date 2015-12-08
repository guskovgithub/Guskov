
text=open('inputFotTask5.txt')

ourWords={}
translate={}

for line in text:
     line = line[:-1].split(' - ')
     line[1] = line[1].split(', ')
     for i in line[1]:
          if i not in translate.keys():
                  translate[i] = [line[0]] 
          else:
                  translate[i].append(line[0])

text.close()
ru_en=open('ru-en.txt', 'w')
for i in sorted(translate.keys()):
       print(i, '-', ', '.join(translate[i]), file = ru_en)
ru_en.close()       
       
