def factorial(n):
    factorial = 1
    for x in range(1,n+1):
        factorial*=x
    return factorial

def lattice_paths(x,y):
    n = x + y
    paths = factorial(n) / (factorial(n - y) * factorial(y))
    return paths
    
paths = lattice_paths(20,20)        
print(paths)
