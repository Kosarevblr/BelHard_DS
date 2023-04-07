# Напишите программу, которая будет открывать определенный файл file и выводить на печать построчно последние строки
# в количестве lines (на всякий случай проверим, что задано положительное целое число)

# line = int(input('Number of lines: '))
# file = input('File name: ')
# if line>0:
#     with open(file) as f:
#         count =0
#         for l in f:
#             f.readline()
#             count+=1
#         for i in (f.readlines()[(count-line):]):
#             print(i)
# else:
#     print('Number of lines is must be >0!')

import pandas as pd

try:
    lines = int(input('Number of lines: '))
    if lines<0:
        raise ValueError
except ValueError:
    print('Number of lines is must be >0!')
try:
    df = pd.read_csv(input('File name: '))
    print(df.tail(lines))
except FileNotFoundError:
    print('No file')
