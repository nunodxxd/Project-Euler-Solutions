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

def rotation(n):
  rotations = set()
  for i in range( len( str(n) ) ):
    m = int( str(n)[i:] + str(n)[:i] )
    rotations.add(m)
  return rotations

def circular_primes(primes):
    circular_primes = set()
    for x in primes:
        rotation_list = rotation(x)
        if set(rotation_list).issubset(primes):
            for item in rotation_list:
                circular_primes.add(item)
    return circular_primes

#Driver code    
primes = SieveOfEratosthenes(1000000)
primes_circular = circular_primes(primes)
        
print(len(primes_circular))
