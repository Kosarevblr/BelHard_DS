# С помощью объектно-ориентированного подхода создайте 4 графика (разместите их в рамках одного изображения)
# установите сетку и легенду для каждого из графиков. для первых 2 графиков(графики А и B) используйте рандомно
# сгенерированные массивы Numpy в качестве данных для осей X и Y. Графики С и D должны демонстрировать обратную
# пропорциональность графикам A и B.

import numpy as np
import matplotlib.pyplot as plt
import random
A = np.array([random.randint(1,10) for _ in range(9)])
B = np.array([random.randint(1,10) for _ in range(9)])
C = np.array([round(3/A[i], 3) for i in range(len(A))])
D = np.array([round(3/B[i], 3) for i in range(len(B))])

fig, axes = plt.subplots(nrows=2, ncols=2)
axes[0][0]=plt.plot(A)
axes[0][1]=plt.plot(B)
axes[1][0]=plt.plot(C)
axes[1][1]=plt.plot(D)
plt.show()
