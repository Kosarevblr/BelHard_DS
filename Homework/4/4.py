# запрашивать пароль пока длина будет не менее 8 символов и не будет содержать имя юзера

name = input('Введите имя: ')
point = 0
password = input('Пароль длинее 8 и без имени: ')
while point == 0:
    if len(password) >= 8 and name not in password:
        print('пароль принят')
        point += 1
        break
    else:
        print('не принят')
        password = input('еще попытка ')
