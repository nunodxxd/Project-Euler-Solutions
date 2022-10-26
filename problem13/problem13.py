string = '37107.......31690'

res = []
for idx in range(0, len(string), 50):
    res.append(int(string[idx : idx + 50]))
num_sum = str(sum(res))

print(num_sum[0 : 10])
