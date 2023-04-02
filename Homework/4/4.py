# запрашивать пароль пока длина будет не менее 8 символов и не будет содержать имя юзера

name = input('Введите имя: ')
password = input('Пароль длинее 8 и без имени: ')
while True:
    if len(password) >= 8 and name not in password:
        print('пароль принят')

        break
    else:
        print('не принят')
        name = input('Введите имя: ')
        password = input('еще попытка ')
