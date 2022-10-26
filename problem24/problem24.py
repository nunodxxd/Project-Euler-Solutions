from itertools import permutations

digit = [0,1,2,3,4,5,6,7,8,9]

listToStr = sorted(''.join(str(elem)) for elem in permutations(digit))

print(listToStr[999999])
