def pythagorean_triplet(n):
    for i in range(1,int(n/3)+1):
        for j in range(i+1,int(n/2)+1):
            k = n-i-j
            if(k*k == i*i + j*j):
                print(i,",", j,",",k)
    
pythagorean_triplet(1000)
