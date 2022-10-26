sum = 0
for x in range(1,1001):
    sum += pow(x,x)

sum_str = str(sum)    
print(sum_str[len(sum_str)-10:len(sum_str)])
