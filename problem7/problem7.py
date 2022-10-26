def SieveOfEratosthenes(n,x):
    prime_count = 0    
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
        
    for p in range(2, n+1):
        if prime[p]:
            prime_count+=1
            if(prime_count == x):
                print(f"{x}st prime is:",p)
                return
            
    print(f"{x}st prime is greater than:",n)
    print("try increase max_number")

max_number=1000000
prime_to_get=10001
SieveOfEratosthenes(max_number,prime_to_get)
