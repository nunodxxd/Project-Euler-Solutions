sum_squares=0
sum_numbers=0
dif=0
for i in range(1,101):
    sum_squares = sum_squares + i * i
    sum_numbers = sum_numbers + i

dif = (sum_numbers * sum_numbers) - sum_squares
print(dif)
