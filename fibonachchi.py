from math import factorial
def product(k):
    return ((-1)**k) * ((2**k) / factorial(k)) 
e, k = int(input()), 1
summ = 0
while product(k - 1) - product(k + 1) > e:
    summ += product(k)
    k += 1
print(summ)
    

