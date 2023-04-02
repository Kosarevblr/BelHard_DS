# дан список, вывести слова больше 3х символов и слова, расположенные до слова длиной 3 символа


lst = ['snow', 'rain', 'wind', 'sun', 'clouds']
for i in lst:
    if len(i) > 3:
        print(i)
    if len(i) == 3:
        ind = lst.index(i)
        # print(*lst[:lst.index(i)])
        print(ind)
print(lst[:ind])
# print()
# for j in lst:
#     if len(j) > 3:
#         print(j)
#     else:
#         break
