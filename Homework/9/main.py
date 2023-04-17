# def is_cat_here(*args):
#     for elem in args:
#         if isinstance(elem, str):
#             if 'cat' in elem.lower():
#                 return True
#
#
# print(is_cat_here('cadvgds', 'cation', 'sxcat'))

# def is_cat_here(*args):
#     try:
#         for elem in args:
#             if 'cat' in elem.lower():
#                 return True
#     except Exception:
#         print('ne stroka')
#
# # print(is_cat_here(2, 'cadvgds', 'cation', 'sxcat', 1))
#
# def your_fav_col(my_color, **kwargs):
#     if kwargs.get('color') is None:
#         return print(f'My favorite color is {my_color}, whats yours?')
#     return print(f'My favorite color is {my_color}, but {kwargs.get("color")} is good')
#
# your_fav_col('red', **{'1':'red', 'color':'green'})

# ax2+bx+c=0
def myfunc(a,b,c):
    d = b**2 - 4*a*c
    if d>0:
        return f'x1 = {(-b - d**0.5)/(2*a)}, x2 = {(-b + d**0.5)/(2*a) }'
    if d == 0:
        return f'x = {(-b)/2*a }'
    if d<0:
        return 'решений нет'

print(myfunc(3,-14,-5))


