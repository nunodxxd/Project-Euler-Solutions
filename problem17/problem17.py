numbers1 = ['one','two','three','four','five','six','seven','eight','nine']
numbers2 = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
numbers3 = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

#build 1 to 19 list
numbers4 = numbers1 + numbers2 

#build 20 to 99 list
for x in range(0,len(numbers3)):
    numbers4.append(numbers3[x])
    for y in range(0,len(numbers1)):
        numbers4.append(numbers3[x] +' '+ numbers1[y])

#build 100 to 999 list
one_thousand = numbers4.copy()
for k in range(0,len(numbers1)):
    one_thousand.append(numbers1[k] + ' hundred')
    for x in range(0,len(numbers4)):
        one_thousand.append(numbers1[k] +' hundred and '+ numbers4[x])
        
one_thousand.append('one thousand')

#remove spaces and count    
without_spaces = []
for i in one_thousand:
    j = i.replace(' ','')
    without_spaces.append(j)
    
string = ''.join(without_spaces)

print(len(string))
