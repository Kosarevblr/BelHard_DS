# Дана последовательность целых чисел. для каждого числа проверить,
# представляют ли его цифры строго возрастающую послежовательность


def vozr(*args):
    for i in range(len(args)):
        digit = str(args[i])
        prev = 0
        for j in range(len(digit)):

            if int(digit[j])<=prev:
                print(f'У числа {args[i]} цифры не возрастают')
                break
            prev = int(digit[j])
        else:

                print(f'У числа {args[i]} цифры строго возрастают')



vozr(123, 441, 266, 56, 233)