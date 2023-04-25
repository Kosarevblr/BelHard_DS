# функция принимает произвольное кол-во целых чисел и определяет сколько 2значных, 3значных.
# кол-во разрядов определяется в отдельной функции

def numbers():
    sp = list(map(int, input('Enter numbers: ').split()))
    numb2zn =0
    numb3zn = 0

    def count(num):
        coun = 0
        while num > 0:
            num //= 10
            coun += 1
        return coun

    for i in range(len(sp)):
        count(sp[i])
        if count(sp[i]) == 2:
            numb2zn+=1
        elif count(sp[i]) == 3:
            numb3zn+=1
    return print(f'Двухзначных: {numb2zn}\n'
                 f'Трехзначных: {numb3zn}')


numbers()

