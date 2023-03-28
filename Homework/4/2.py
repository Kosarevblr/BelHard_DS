# дана строка, вывести ее до символа "р" включительно, пропуская каждый третий символ

s = 'Break and Continue operators'
s1 = ''
for i in range(0, len(s)):
    if s[i-1] == 'p':
        break
    for j in range(0, len(s),2):
        s1=s[j]


print(s1)

