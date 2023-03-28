# Напишите программу, в которой пользователь вводит целое число
# а программа определяет, сколько в этом числе цифр 0, 1, 2 и так далее
# до 9.

n = input('Целое число: ')
lst = [n[i] for i in range(len(n))]
mn = list(set(lst))
mn.sort()
for i in range(len(mn)):
    print(f'Кол-во {mn[i]} = {lst.count(mn[i])}')
