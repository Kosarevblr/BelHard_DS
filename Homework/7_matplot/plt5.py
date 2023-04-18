# Назвать график, обозначить оси, рассчитать среднеквадратичное отклонение,
# построить график и сохранить его в формате jpeg.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv('E:\python DS\electrons in plasma.csv', usecols=['X', 'Y'])
x = [float(el.replace(',','.')) for el in df['X']]
y = [float(el.replace(',','.')) for el in df['Y']]
plt.xlabel('Ось Х')
plt.ylabel('Ось У')
plt.title('Электроны в плазме')
plt.plot(x, y)
plt.savefig('electrons.jpeg')
plt.show()

npx = np.array(x).std()
npy = np.array(y).std()
print(npx, npy)