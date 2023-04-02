import random
n = input('Enter lenght: ')
try:
    n = int(n)
except TypeError as e:
    print('not number')
    n = input()
lst=[]
for i in range(len(n)):
    lst.append(random.randint(0,10))
iterat = iter(lst)
for i in range(len(n)+1):
    try:
        print(next(iterat))
    except StopIteration as e:
        print('The end')
        break