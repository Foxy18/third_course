from math import*
def square(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c))**0.5

def input_side_and_search_square():
    a, b, c = map(float, input('Введите длины сторон треугольника через пробел:').split())
    return square(a, b, c)
    

if __name__ == "__main__":
    squares = []
    for _ in range(3):
        squares.append(input_side_and_search_square())
    print(max(squares))
    