# Дана последовательность целых чисел. найти в каждом числе сумму четных цифр


def chet(*args):
    for i in range(len(args)):
        s = 0
        for (x) in str(args[i]):
            if int(x) % 2 == 0:
                s += int(x)
        print(f'У числа {args[i]} сумма четных равна {s}')


chet(122, 441, 266, 56, 123)
