num=1
n=2
diagonal_numbers=[1]
while num < 1001*1001:
    for x in range(1,5):
        num+=n
        diagonal_numbers.append(num)
    n+=2
        
print(sum(diagonal_numbers))
