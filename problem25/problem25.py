n1 = 1
n2 = 1
x=3
while True:
    fib = n1 + n2
    n1 = n2 
    n2 = fib
    if len(str(fib)) == 1000:
        print(x)
        break
    x+=1
