list = ["MARY",.....,"ALONSO"]
list_values = []

list.sort()

for idx, word in enumerate(list):
    value = 0
    for digit in word:
        value += ord(digit)-64
    value = value * (idx+1)
    list_values.append(value)

print(sum(list_values))
