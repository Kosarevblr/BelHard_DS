# дана строка, вывести ее до символа "р" включительно, пропуская каждый третий символ

s = 'Break and Continue operators'

for index, char in enumerate(s):
    if index % 3 == 0 and index != 0:
        continue
    if char == 'p':
        print(char, end='')
        break
    print(char, end='')
