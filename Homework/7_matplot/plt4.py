# Важно уметь отобразить данные уравнения на графике. В качестве уравнения мы будем использовать очень известное
# уравнение: E=mc2
# С помощью Ваших знаний Numpy создайте два массива:
# E и m: значения m - это 11 равноотстоящих друг от друга чисел от 0 граммов до 10 граммов значения E должны быть равны
# энергии для этих масс.
# Вам нужно будет указать значение для c, приведя его в нужные единицы измерения - в метрах в секунду, построить график,
# где ось X - масса в граммах, ось Y - энергия в Дж. Также добавьте сетку для графика и сохраните изображение
# в формате svg.  c= 299 792 458 m/c

import matplotlib.pyplot as plt
import numpy as np
c = 299792458
m = np.array([i for i in range(11)])
m_kg = np.array([i/1000 for i in m])
e = np.array([m*c**2 for m in m_kg])
plt.plot(m,e)
plt.xlabel('Масса, грамм')
plt.ylabel("Энергия, Джоуль")
plt.grid(True)
plt.savefig('mc.svg')
plt.show()