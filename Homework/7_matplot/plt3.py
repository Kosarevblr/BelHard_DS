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
axes[0][0].plot(A)
axes[0][0].set_title('график А')
axes[0][0].set_xlabel('X')
axes[0][0].set_ylabel('Y')
axes[0][0].grid(True)
axes[0][1].plot(B)
axes[0][1].set_title('график B')
axes[0][1].set_xlabel('X')
axes[0][1].set_ylabel('Y')
axes[0][1].grid(True)
axes[1][0].plot(C)
axes[1][0].set_title('график C')
axes[1][0].set_xlabel('X')
axes[1][0].set_ylabel('Y')
axes[1][0].grid(True)
axes[1][1].plot(D)
axes[1][1].set_title('график D')
axes[1][1].set_xlabel('X')
axes[1][1].set_ylabel('Y')
axes[1][1].grid(True)

fig.suptitle("Одна зона для всех графиков",fontsize=15)
fig.subplots_adjust(left=None,
    bottom=None,
    right=None,
    top=None,
    wspace=0.5,
    hspace=0.5,)
plt.show()
