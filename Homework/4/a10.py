# Создать матрицу 3*3, заполнить ее рандомными значениями. Заменить все четные числа на нули.

import numpy as np
import random

# m=np.array([[random.randint(0,100) for _ in range(3)],
#             [random.randint(0,100) for _ in range(3)],
#             [random.randint(0,100) for _ in range(3)]])


m = np.array([[random.randint(0, 100) for j in range(3)] for i in range(3)])
print(m)

new_m = [0*elm if elm%2==0 else elm for elm in m]     почему не работает?

for index, item in enumerate(m):
    if item%2==0:
        m[index] = 0
#
m[m % 2 == 0] = 0
print(m)