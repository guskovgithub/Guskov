
text=open('inputFotTask5.txt')
ourWords={}
for line in text:
    line=line.replace('','').replace('  ','').replace('.','').replace('\n','').split('-')
    print(line)
    ourWords[line[0]]=line[1]
text.close()

