#More infos:
#https://mathworld.wolfram.com/AnomalousCancellation.html
#https://oeis.org/A259981
#https://www.educative.io/answers/project-euler-33-digit-canceling-fractions

#note: This code is not mine, I just found it while I was looking for it. I decided to share because it is a very good solution. All rights reserved to Armaan Nougai and educative.io.

def gcd(a,b):
    b,a = min((a, b)), max((a, b))
    if a%b == 0: return b
    
    # if any of a or b is odd, then we will skip all odd factors
    any_odd = (a|b)%2                   
    hcf = 1
    for j in range(2 + any_odd, b//2 + 1, 1 + any_odd):
        print('checking',j)
        if b%j == 0 and a%j == 0:
            hcf = j
    return hcf

# num/den is the multiplication of all curious fraction less than 1
num = 1
den = 1

# i is digit to be cancelled
for i in range(1, 10):
    # d is remaining digit in denominator
    for d in range(1, i):
        # n is remaining digit in numerator
        for n in range(1, d):
            if 10*n*d + i*d == 10*i*n + d*n:
                num *= 10*n + i
                den *= 10*i + d

common_term = gcd(num, den)

print(den//common_term)
