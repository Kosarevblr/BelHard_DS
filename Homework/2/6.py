# Вычислить индекс массы (ИМТ = масса в кг/ (рост в метрах возвести
# в квадрат) )I = weight / height тела в зависимости от роста, веса
# и возраста, а затем проинтерпретировать результат в соответствии с
# рекомендациями Всемирной Организации Здравоохранения:

m = int(input('Vvedi ves (kg): '))
n = float(input('Vvedi rost (m): '))
age = int(input('Vvedi vozrast: '))
imt = m / n ** 2
if age < 45:
    if imt < 18.5:
        print("not enough")
    if 18.5 <= imt <= 24.99:
        print('normal')
    if 25 <= imt <= 29.99:
        print('too much')
    if imt >= 30:
        print('tooooooo faaaaaaat')
else:
    if imt < 22:
        print("not enough")
    if 22 <= imt <= 26.99:
        print('normal')
    if 27 <= imt <= 31.99:
        print('too much')
    if imt >= 32:
        print('tooooooo faaaaaaat')
