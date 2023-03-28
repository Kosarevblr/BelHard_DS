 # дан список, вывести слова больше 3х симаолов и слова, расположенные дослова длиной 3 символа


lst = ['snow', 'rain', 'wind', 'sun', 'clouds']
for i in lst:
    if len(i)>3:
        print(i)
print()
for j in range(len(lst)):
    if len(lst[j])>3:
        print(lst[j])
    else:
        break