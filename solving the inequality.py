#Составить программу решения неравенства ax ≥b, где a, b –параметры, значения которых задаются с клавиатуры.
a, b = map(float, input('Введите коэффициенты a и b для неравенства ax ≥ b через пробел: ').split())
if a > 0:
    print(f'x ∈ [{b / a}; +∞)')
elif a < 0 and b == 0:
    print('x ∈ (-∞; 0]')
elif a < 0 and b != 0:
    print(f'x ∈ (-∞; {b / a})')
elif a == 0 and b > 0:
    print('x ∈ ø')
else:
    print('x ∈ (-∞; +∞)')
