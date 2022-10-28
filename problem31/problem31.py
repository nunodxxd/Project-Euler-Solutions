sum = 200
coins = [1,2,5,10,20,50,100,200]

table = [0 for k in range(200+1)]
table[0] = 1

for i in range(0,len(coins)):
    for j in range(coins[i],sum+1):
        table[j]+= table[j-coins[i]]
        
print(table[sum])
