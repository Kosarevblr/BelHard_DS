# проверка логина и пароля для входа в систеиу. ф-ция с параметрами: имя пользователя, пароль,
# кол-во попыток входа (по умолчанию - 3), ссобщение после 3х неудачных попыток

def sys_enter():
    name_default = 'myname'
    password_default = 'mypass'
    tries = 3
    while tries > 0:
        name = input()
        password = input()
        if name == name_default and password == password_default:
            return print('Добро пожаловать в систему')
        else:
            tries -= 1
            print('Неверное имя или пароль')

    return print('Система заблокирована')

sys_enter()