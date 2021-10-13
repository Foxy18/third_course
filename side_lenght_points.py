def input_point(line):
    #преобразование координат точки в список
    x, y= map(int, line[1: -1].split(","))
    return [x, y]

def side_lenght(A, B):
    return ((B[0] - A[0])**2 + (B[1] - A[1])**2)**0.5


if __name__ == "__main__":
    A, B, C = map(input_point, input('Введите координаты точек через пробел в формате (x,y): ').split(' '))
    print(f'Длина стороны АВ = {side_lenght(A, B)}')
    print(f'Длина стороны BC = {side_lenght(B, C)}')
    print(f'Длина стороны АC = {side_lenght(A, C)}')
