def fibonachchi(n):
    a, b = 1, 1   
    for _ in range(1, n):
        k = a 
        print(k, end = ' ')
        a, b = b, a + b
    return k
 
fibonachchi(int(input()))

