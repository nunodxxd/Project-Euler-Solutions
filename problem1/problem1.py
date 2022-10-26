mutiples = []
for x in range(0,1000):
    if x%3 == 0 or x%5 == 0:
        mutiples.append(x)
        
print(sum(mutiples))
