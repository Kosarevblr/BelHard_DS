# Запросить у пользователя данные (имя, фамилия, возраст) и создать файл с этими значениями.

import pandas as pd
name = input('Enter name: ')
sur = input('Enter surname: ')
age = input('Enter age: ')
data = {'name': [name], 'surname': [sur], 'age': [age]}
df = pd.DataFrame(data)
df.to_csv('name_surn.csv', mode='w', index=False)
