def even_odd(num):
    if num % 2 == 0:
        return num/2
    else:
        return 3*num+1

def collatz_sequence(n):
    sequence = []
    while True:
        if n == 1:
            sequence.append(int(n))
            break
        else:
            sequence.append(int(n))
            n = even_odd(n)
    return sequence
    
bigger_sequence=[]    
for x in range(1,1000000):
    sequence = collatz_sequence(x)
    if len(sequence) > len(bigger_sequence):
        bigger_sequence = list(sequence)
        
print(bigger_sequence)
