def divisors(n):
    divs = [1]
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            divs.extend([i,int(n/i)])
    divs.extend([n])
    return list(set(divs))
    
def abundant_nums(n):
    abundant = []
    for x in range(1,n+1):
        divs = divisors(x)
        if sum(divs) > 2*x:
            abundant.append(x)
    return sorted(abundant)

def all_sum_of_two_abundants(abundants):
    sum = set()
    for x in abundants:
        for y in abundants:
            if x+y > 28123:
                break
            sum.add(x+y)
    return sum
    
abundants = abundant_nums(28123)
sum_abundants = all_sum_of_two_abundants(abundants)
final_set = set(range(0, 28124)) - sum_abundants
print(sum(final_set))
