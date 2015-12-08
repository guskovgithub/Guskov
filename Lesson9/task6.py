en_ru = open('en-ru6.txt')
ru_en = open('ru-en6.txt')
en_ru_new={}
ru_en_new={}
''' en-ru dict'''
for line in en_ru:
     line = line[:-1].split(' - ')
     for i in line[0].split(','):
        if i not in en_ru_new.keys():
           en_ru_new[i] = [line[1]]
        else:
           en_ru_new[i].append(line[1])    
     for i in line[1].split(','):
        if i not in ru_en_new.keys():
           ru_en_new[i] = [line[0]]
        else:
           en_ru_new[i].append(line[0])   

'''ru-en dict'''
for line in ru_en:
     line = line[:-1].split(' - ')
     
     for i in line[1].split(','):
        if i not in en_ru_new.keys():
           en_ru_new[i] = [line[0]]
        else:
           
           en_ru_new[i].append(line[0])   
     for i in line[0].split(','):
        if i not in ru_en_new.keys():
           ru_en_new[i] = [line[1]]
        else:
           
           ru_en_new[i].append(line[1])   
print('!!! en-ru dictionary !!!')           
for i in sorted(en_ru_new.keys()):
   print(i,' - ', en_ru_new[i])          
print('!!! ru-en dictionary !!!')
for i in sorted(ru_en_new.keys()):
   print(i,' - ', ru_en_new[i])



en_ru.close()
ru_en.close()    
        
