def factorial(n):
    factorial=1
    for x in range(1,n+1):
        factorial *= x        
    return factorial

def factorial_digit_sum(n):
    sum=0
    for x in str(n):
        sum += int(x)
    return sum
    
reslt = factorial(100)
sum_reslt = factorial_digit_sum(reslt)

print(sum_reslt)
