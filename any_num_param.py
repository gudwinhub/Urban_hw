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

any_num_parm(11) # задаем значение параметра a, параметр b= по умолчанию
print('')
any_num_parm(111, 222) # задаем а и b
print('')
any_num_parm(111, *lst) # задаем а, b = первому элементу из списка
print('')
any_num_parm(111, 22, *lst)
print('')

dict = {'d1':333, 'd2':True, 'd3':'строка'}

any_num_parm(2, dict) # b = по умолчанию, далее словарь попадет в args
print('')
any_num_parm(2, **dict) # b = по умолчанию, далее словарь попадет в kwargs
print('')
any_num_parm(2, 22,  dict) # задаем значения параметров a, b  словарь попадает в args
print('')
any_num_parm(2, 22, **dict) # словарьь попадает в kwargs
