def any_num_parm(a, b=2, *args, **kwargs):
    print('параметр a = ', a, '\n', 'параметр b = ', b)
    if not args:
        print(' args не передавались')
    else:
        print('args = ', args) # печать списком
        print('args = ', *args) # печать поэлементно
    if not kwargs:
        print(' kwargs не передавались')
    else:
        print('kwargs = ', kwargs)
        for value in kwargs.values():
            print(value, sep = ' ')


lst = 1, 2, 3, 4, 5

# any_num_parm(11) # позиционные параметры
# print('')
# any_num_parm(111, 222)
# print('')
# any_num_parm(111, *lst)
# print('')
# any_num_parm(111, 22, *lst)
# print('')

dict = {'d1':333, 'd2':True, 'd3':'строка'}

any_num_parm(2, 2, [], dict) # позиционные параметры + упакованные + именованные
# print('')
any_num_parm(111, 222,[], **dict) # позиционные параметры + упакованные + именованные
