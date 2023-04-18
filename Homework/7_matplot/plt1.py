import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(r'C:\Users\Trollolord\PycharmProjects\BelHard_DS\Homework\7\data - Лист1 - data - Лист1.csv',
                 usecols=['X', "Y"])
x = [float(el.replace(',','.')) for el in df['X']]
y = [float(el.replace(',','.')) for el in df['Y']]
plt.xlabel('Ось Х')
plt.ylabel('Ось У')
plt.title('Зависимость Х от У')
plt.plot(x, y)
plt.show()
plt.savefig('plot.jpg')
npx = np.array(x).std()
npy = np.array(y).std()
print(npx, npy)