# Будет текстовый файл с числами которые нужно использовать для создания массива.

import numpy as np

with open('text.txt') as f:
     data = f.read().split()

matr = np.array(data).reshape(3,3)
print(matr)