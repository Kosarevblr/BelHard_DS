# Будет СЛАУ которую нужно решить методом Гаусса/Крамера.
# пример: 5х1 + 2х2 = 7
#         2х1 + х2 = 9


import numpy as np

matr1 = np.array([[5, 2], [2, 1]])
matr2 = np.array([7, 9])
res = np.linalg.solve(matr1, matr2)

print(res)