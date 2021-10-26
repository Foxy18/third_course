from math import factorial
def product(k):
    return ((-1)**k) * ((2**k) / factorial(k)) 


e, k = float(input()), 1
summ = 0
while abs(product(k)) > e:
    summ += product(k)
    k += 1
print(summ)
    

