number = 0
while(True):
    for i in range(20,0,-1):
        number+=1
        if number%i != 0:
            break
    if i==1:
       print(number+1)
       break
