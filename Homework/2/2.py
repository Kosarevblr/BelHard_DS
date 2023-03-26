#  найти кол-во уникальных цфифр, макс и мин цифру из чисел:

# a=str(543731)
# b=str(4472)
# c=str(999999)
# d=str(347623)
# e=str(1000001)
#
# print(set(a), len(set(a)), max(set(a)), min(set(a)))
# print(set(b), len(set(b)), max(set(b)), min(set(b)))
# print(set(c), len(set(c)), max(set(c)), min(set(c)))
# print(set(d), len(set(d)), max(set(d)), min(set(d)))
# print(set(e), len(set(e)), max(set(e)), min(set(e)))

lst = [543731, 4472, 999999, 347623, 1000001]
for i in lst:
    digit = set(str(i))
    print(digit, len(digit), min(digit), max(digit), sep='---')
