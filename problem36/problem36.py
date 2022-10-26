def reverse(n):
    if type(n) is int:
        num_string = str(n)
    else:
        num_string = n
    size = len(num_string)
    reversed_num = num_string[size::-1]  
    return reversed_num

palindromic = set()
for num in range(1,1000000):
    binary = bin(num).replace("0b", "")
    reversed_binary = reverse(binary)
    reversed_num = reverse(num)
    if str(num) == reversed_num and binary == reversed_binary:
        palindromic.add(num)

print(sum(palindromic))
