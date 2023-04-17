# def myfunc(name: str) -> str:
#     return f'Hello, {name}'
#
# print(myfunc(input()))

# def cat_voice() -> str:
#     return 'Meow'
#
#
# def dog_voice() -> str:
#     return 'Woof'
#
#
# print(cat_voice)
# print(dog_voice)


# def get_voice(text: str) -> str:
#     return text+'!!!!'
#
# print(get_voice(input()))
#
# def myfunc(a,b: int) -> list:
#     number = []
#     for elem in range( a, b+1):
#         if elem%2!=0:
#             number.append(elem)
#
#     return number
#
# print(myfunc(int(input()), int(input())))

# import random
# def myfunc(a,b, lenght: int) -> list:
#     number = []
#
#     while len(number) != lenght:
#         i = random.randint(a,b)
#         if i%2!=0:
#             number.append(i)
#     return number
#
# print(myfunc(int(input()), int(input()), int(input())))

import random
# def myfunc(a,b: int) -> list:
#
#     return [i for i in range(a,b+1) if i%2!=0]
#
# print(myfunc(12, 24))

# x = lambda name: f'hello {name}'
# print(x('sdfsdf'))

# lst = ['1','33','5555','3333']
# print(list(map(len, lst)))

lst = [1, 3, 444, 555555]
print(list(map(float, lst)))