triangle = [59,73,...,63,35]

def max_path_sum(rows,list):
    for x in range(rows-1,0,-1):
        for y in range((x * (x-1))//2,(x*(x+1))//2):
            list[y] += max(list[y+x], list[y+x+1])
    print(list[0])   
    
max_path_sum(100,triangle)
