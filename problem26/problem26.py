#https://mathworld.wolfram.com/FullReptendPrime.html

def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
       
    primes = set()
    for p in range(2, n+1):
        if prime[p]:
            primes.add(p)
    return primes
  
def FullReptendPrime(n):
    for x in range(1,n):
        if (10**x)%n == 1:
            if x != n-1:
                return False
            else:
                return True
    return False

primes = sorted(SieveOfEratosthenes(1000))
for x in reversed(primes):
    if FullReptendPrime(x):
        print(x)
        break
