import itertools
import random

with open('test1.txt', 'w+') as f:
    for _ in range(10):
        f.write(str(random.randint(0,10)))
        f.write('\n')
    # f.writelines(str(random.randint(0,10)) for _ in range(10))    слипается в 1 строку
    f.seek(0)
    data = f.read().splitlines()
with open('test2.txt', 'w') as file:
    for i in itertools.combinations(data, 2):
        file.write(''.join(i)+'\n')

