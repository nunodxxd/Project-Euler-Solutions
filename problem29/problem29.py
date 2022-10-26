nums = set()
for x in range(2,101):
    for y in range (2,101):
        term = x**y
        if term not in nums:
            nums.add(term)

print(len(nums))
