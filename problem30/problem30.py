sum=0
list=[]

#change from 999999 to 6*9**5 after read Semtex solution 
for x in range(2,6*9**5):
    sum_pow = 0
    for digit in str(x):
        sum_pow += pow(int(digit),5)
    if sum_pow == x:
        sum += sum_pow
        list.append(x)

print(list)
print(sum)
