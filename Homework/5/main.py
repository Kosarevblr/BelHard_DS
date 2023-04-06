# import random
# n = input('Enter lenght: ')
# try:
#     n = int(n)
# except TypeError as e:
#     print('not number')
#     n = input()
# lst=[]
# for i in range(len(n)):
#     lst.append(random.randint(0,10))
# iterat = iter(lst)
# for i in range(len(n)+1):
#     try:
#         print(next(iterat))
#     except StopIteration as e:
#         print('The end')
#         break

# with open('nums.txt', 'r') as f:
#     data = f.readlines()
#     print(data)
#     print(len(data))

# with open('nums.txt', 'r+') as f:
#     data = f.readlines()
#     data[0] = 'asfdasda'
#     f.seek(0)
#     f.writelines(data)

import pandas as pd
df = pd.read_csv('example.csv')
print(df)
a = df.hist('x')
print(a)