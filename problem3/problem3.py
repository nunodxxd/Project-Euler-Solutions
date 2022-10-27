number = 600851475143
factor = 2

while factor<=number:
    if number%factor == 0:
        maxfactor = factor
        number = number / factor
    else:
        factor +=1
    
print(maxfactor)
