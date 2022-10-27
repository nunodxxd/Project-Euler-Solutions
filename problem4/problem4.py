list = []
for i in range(1, 999):
    for j in range(1, 999):
        x = i * j
        reverse = str(x)[::-1]
        if x == int(reverse):
            list.append(x)

print(max(list))
