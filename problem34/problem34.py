import math 

nums = set()
for x in range(3,100000):
    sum_fact = 0
    for digit in str(x):
        sum_fact += math.factorial(int(digit))
    if sum_fact == x:
        nums.add(x)

print(sum(nums))
