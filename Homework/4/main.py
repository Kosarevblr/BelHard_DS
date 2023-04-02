# class MyException(Exception):
#     pass

#
# a, b = input('1 numb'), input('2 numb')
# try:
#     a = float(a)
#     b = float(b)
#
# except Exception as e:
#     print(e)
#     # raise MyException('wrong choise')
#
# else:
#     print(a+b)
# finally:
#     print('job is done')

a, b = input('1 numb: '), input('2 numb: ')
c = input('operation: ')
operation = ['-', '+', '/', '*']
if c not in operation:
    raise KeyError('оператор не поддерживается')
else:
    a2_is_num = True
    b2_is_num = True
    try:
        a1 = float(a)
        b1 = float(b)
    except Exception as e:
        try:
            a2 = float(a)
        except Exception as e:
            a2_is_num = False
        try:
            b2 = float(b)
        except Exception as e:
            b2_is_num = False
    if a2_is_num is True and b2_is_num is True:
        res = a+b
        print(res)

    if operation == '+':
        print(a + b)
    if operation == '/':
        try:
            res = a / b
        except ZeroDivisionError as e:
            print('На ноль делить нельзя')
        else:
            print(res)
        finally:
            print('Готово')
