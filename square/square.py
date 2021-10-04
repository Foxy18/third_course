def square(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c))**0.5

def input_side():
    a, b, c = map(float, input('Введите длины сторон треугольника через пробел:').split())
    return [a, b, c]
    

if __name__ == "__main__":
    squares = []
    for _ in range(3):
        a, b, c = input_side()
        squares.append(square(a, b, c))
    print(max(squares))
    