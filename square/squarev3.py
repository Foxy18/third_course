def square(a, b, c):
    return abs(((a[0] - c[0]) * (b[1] - c[1]) - (b[0] - c[0]) * (a[1] - c[1])) / 2)

def input_point(line):
    #преобразование координат точки в список
    x, y= map(int, line[1: -1].split(","))
    return [x, y]
    

if __name__ == "__main__":
    squeres=[]
    A, B, C, D = map(input_point, input('Введите координаты точек через пробел в формате (x,y): ').split(' '))
    squeres.append(square(A, B, C))
    squeres.append(square(A, C, D))
    print(square(B, C, D))
    squeres.append(square(A, B, D))
    squeres.append(square(B, C, D))
    print(max(squeres))