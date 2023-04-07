# Напишите программу в которой создается текстовый файл. Имя файла вводится пользователем.
# Текст для файла вводится пользователем. При записи текста в файл все маленькие буквы заменяются на большие.

name = input('Enter file name: ')
fullname = name+'.txt'
with open(fullname, 'w') as f:
    text = input('Enter text: ').upper()
    f.write(text)
