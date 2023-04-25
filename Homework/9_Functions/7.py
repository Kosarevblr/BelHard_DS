# есть диапазон чисел. найти факториал каждого третьего простого числа из диапазона
import math


def prost(*args):
    new_n = []
    for num in args:
        counter = 0
        for i in range(1, num + 1):
            if num % i == 0:
                counter += 1
        if counter == 2:
            new_n.append(num)
    f =[]
    for i in range(0, len(new_n), 2):
        f.append(math.factorial(new_n[i]))
    return print(f)


prost(1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17)
