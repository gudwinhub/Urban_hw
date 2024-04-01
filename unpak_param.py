def print_param(a, b, c):
    # if
    print('a = ',a , 'b = ',b, 'c =', c, sep=  '\n')

def print_param2(*my_param):
    print('my_param =', my_param )


val_lst = [123, 'строка', True]
val_dict = {'a':123, 'b':'строка', 'c':True}
val_lst2 = [11, True]

# print_param(*val_lst)
# print_param(**val_dict)
#
# print_param(*val_lst2, 42)

print_param(val_lst, 11) # ПЕЧАТАЕТ 1-й параметр нераспакованый список, 2-й число 11
print_param2(*val_lst, 11) # печатает распакованный список и в конец списка добавляет число 11