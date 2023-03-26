# По длинам трех отрезков, введенных пользователем, определить
# возможность существования треугольника, составленного из этих
# отрезков. Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или
# равносторонним.

a, b, c = int(input()), int(input()), int(input())
if a + b > c and a + c > b and b + c > a:
    print('exist')
    if a == b == c:
        print('all sides are equal')
    if a != b != c:
        print('all sides are different')
    else:
        print('2 sides are equal')
else:
    print('not exist')