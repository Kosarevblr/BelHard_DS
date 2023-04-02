# Напишите программу для решения квадратного уравнения. В процессе поиска решения использовать
# обработку исключительных ситуаций.

print('Ax**2+Bx+C=0')

try:
    a = int(input('A: '))
    b = int(input('B: '))
    c = int(input('C: '))
except ValueError:
    print('Введи числа!')
    a = int(input('A: '))
    b = int(input('B: '))
    c = int(input('C: '))

D = b ** 2 - 4 * a * c
if D < 0:
    print('Корней нет')
elif D == 0:
    print(f'x={-b / (2 * a)}')
else:
    print(f'x1={(-b + D ** 0.5) / (2 * a)}, x2={(-b - D ** 0.5) / (2 * a)}')
