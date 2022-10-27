def fibonacci(x): 
    num=0
    n1,n2=1,2
    fibonacci = [1,2]
    while True:
        num = n1+n2
        n1=n2
        n2=num
        if num > x:
            break
        fibonacci.append(num)  
    return fibonacci

def even_numbers(fibo):
    even_list = []
    for x in fibo:
        if x%2 == 0:
            even_list.append(x)
    return even_list    
    
fibo = fibonacci(4000000)
even_nums = even_numbers(fibo)
print(sum(even_nums))
