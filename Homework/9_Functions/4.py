# Дана последовательность целых чисел. найти количество делителей для каждого числа

num = [12, 44, 2, 56, 123]

def count(num):
    div = list(filter(lambda x: num % x == 0, range(1, num+1)))
    return len(div)
for i in range(len(num)):
    kolvo = count(num[i])
    print(f'У числа {num[i]} {kolvo} делителей')