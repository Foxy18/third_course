x = float(input('Введите значение аргумента функции: '))
if -7 <= x <= -6:
    print('y = 1')
elif -6 < x <= -4:
    print(f'y = {"%.2f" % (x / 2 + 2)}')
elif -4 < x <= 0:
    print(f'y = {"%.2f" % ((4 - (x + 2)**2)**0.5)}')
elif 0 < x < 2:
    print(f'y = {"%.2f" % (-(1 - (x - 1)**2)**0.5)}')
elif 2 <= x <= 3:
    print(f'y = {"%.2f" % (-x + 2)}')
else:
    print('Введите значение х, принадлежащее промежутку от -7 до 3')
