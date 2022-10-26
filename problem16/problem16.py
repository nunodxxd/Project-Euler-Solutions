num = int(input('Enter number:'))
pow = int(input('Enter power:'))

rslt = num**pow
digits=[]

for x in str(rslt):
    digits.append(int(x))
    
print(sum(digits))
