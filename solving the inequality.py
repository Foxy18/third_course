a, b = map(float, input('Введите коэффициенты a и b для неравенства ax ≥ b через пробел: ').split())
if a > 0:
    print(f'x ∈ [{b / a}; +∞)')
elif a < 0:
    print(f'x ∈ (-∞; {b / a}]')
elif a == 0 and b > 0:
    print(f'x ∈ ø')
elif a == 0 and b <= 0:
    print('x ∈ (-∞; +∞)')
else:
    print('Введите корректные значения коэффициентов')