# import numpy as np
#
# a = np.random.randint(0,10, (3,3))
# print(a)
# b = a.transpose()
# print(b)
# res = np.dot(a,b)
# print(res)

# import itertools
# lst = ['red', 'green', 'white', 'black']
# for i in itertools.permutations(lst, 3):
#     print(' '.join(i))
#
# import random
#
# old_g = 0
# both_g = 0
# mlad_g = 0
# either = 0
# kids = ['boy', 'girl']
# for i in range(10000):
#     younger = random.choice(kids)
#     older = random.choice(kids)
#     if older == kids[1]:
#         old_g += 1
#     elif younger == kids[1] and older == kids[1]:
#         both_g += 1
#     elif older == kids[1] or younger == kids[1]:
#         either += 1
# print(print(f'old {old_g}, both {both_g}')...........
#

# Создать массив NumPy, наполнить его случайными значениями,
# транспонировать массив, рассчитать среднеквадратичное отклонение элементов массива, вычислить определитель

# import numpy as np
# import random
#
# A = np.random.randint(0, 10, (3, 3))
# B = np.transpose(A)
# d = np.linalg.det(A)
# c = np.std(A)
# print(A, B, d, c, sep='\n')

# Создать массив NumPy, вычислить сумму элементов массива,
# минимальный и максимальный элемент массива, количество элементов в массиве и вычислить дисперсию элементов массива.

# import numpy as np
# A = np.random.randint(0, 10, (3, 3))
# s = np.sum(A)
# amin = np.min(A)
# amax = np.max(A)
# alen = np.size(A)
# disp = np.var(A)
# print(A, s, amin, amax, alen, disp, sep = '\n')

import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3]
y = [4, 5, 6]
plt.plot(x, y)
