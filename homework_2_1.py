# Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# Используйте комплексные числа
# для извлечения квадратного корня.

a = float(input('\nВведите число а: '))
b = float(input('\nВведите число b: '))
c = float(input('\nВведите число c: '))

d = b ** 2 - 4 * a * c
result = ''

if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    result = f'\nУравнение имеет два вещественных корня: ({round(x1, 3)}, {round(x2, 3)})'

elif d == 0:
    x = -b / (2 * a)
    result = f'\nУравнение имеет один вещественный корень: {(x)}'
else:
    d = complex(d, 0)
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    result = f'\nУравнение имеет два комплексных корня: ({"{:g}".format(x1)}, {"{:g}".format(x2)})'

print(result)
