import math
def getDivisors(n) :
    divisor_count=0
    i = 1
    while i <= math.sqrt(n):
        if (n % i == 0) :
            if (n / i == i) :
                divisor_count+=1
            else :
                divisor_count+=2
        i = i + 1
    return divisor_count



i=1
while True:
    triangle_number=(i*(i+1))/2
    i+=1
    divisors = getDivisors(triangle_number)
    if divisors >= 500:
        print(triangle_number)
        break
