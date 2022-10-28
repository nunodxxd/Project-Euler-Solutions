
def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
       
    primes = []
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)
    return primes

def is_prime(n):
	for i in range(2,int(abs(n)**0.5)+1):
		if n%i == 0:
			return False
	return True

prime_nums = SieveOfEratosthenes(1000)
primes = prime_nums.copy()

largest = 0
for b in prime_nums:
	for a in prime_nums:
		i = 0
		while True:
			quadratic = i**2+a*i+b
			if quadratic not in primes:
				if is_prime(quadratic):
					primes.append(quadratic)
				else:
					if i-1 > largest:
						largest = i-1
						axb = a*b
					break
			i += 1
		i = 0
		while True:
			quadratic = i**2-a*i+b
			if quadratic not in primes:
				if is_prime(quadratic) and quadratic>0:
					primes.append(quadratic)
				else:
					if i-1 > largest:
						largest = i-1
						axb = -1*a*b
					break
			i += 1

print(axb)

