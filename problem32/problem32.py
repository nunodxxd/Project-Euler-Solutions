pandigital = {'1','2','3','4','5','6','7','8','9'} 

final = set()

for x in range(9):
    for  y in range(999,9999):
        size = str(x) + str(y) + str(x * y)
        if len(size) > 9: break
        if len(size) == 9 and pandigital == set(size):
            final.add(x * y)
        
            
for x in range(99):
    for  y in range(99,999):
        size = str(x) + str(y) + str(x * y)
        if len(size) > 9: break
        if len(size) == 9 and pandigital == set(size):
            final.add(x * y)
            
print(sum(final))
