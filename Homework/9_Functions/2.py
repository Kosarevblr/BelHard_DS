# функция, принимающая сведения об авторе

def author_info(kwargs):

    name = kwargs.get('name', '?')
    surname = kwargs.get('surname', '?')
    patronymic = kwargs.get('patronymic', 'Not found')
    birthdate = kwargs.get('birth_date', '?')
    deathdate = kwargs.get('death_date', '?')
    info = kwargs.get('info', 'Not found')

    fullname = f'{name[0]}.{patronymic[0]}.{surname}'
    dateoflife = f'({birthdate} - {deathdate})' if birthdate and deathdate else ''

    return print(f'{fullname} {dateoflife} - {info}')

author_info({
        'name': input('Имя: '),
        'surname': input('Фамилия: '),
        'patronymic': input('Отчество: '),
        'birth_date': input('Дата рождения: '),
        'death_date': input('Дата смерти: '),
        'info': input('Информация: ')
    })