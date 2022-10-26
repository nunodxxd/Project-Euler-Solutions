def SieveOfEratosthenes(n):
    prime_sum = 0    
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
        
    for p in range(2, n+1):
        if prime[p]:
            prime_sum += p
    print(prime_sum)


max_number=2000000

SieveOfEratosthenes(max_number)
