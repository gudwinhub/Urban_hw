
#  Получить ключ по значению
d = {1: False, 2: False, 3: False, 4: False }
#  замена/ добавление нового значения
#  dict[key] = value # если key отсутствует то добавляется новая пара key: value

# print(False in tables.values())


value = True

# вариант 1
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

print(get_key(d, value))
# print(get_key(d, '2'))
# print(get_key(d, 42))
# print()
# print([key: val for key, val in range(5)])
#
# val: bool = False
# # dict = {key: val for key in range(1, 5)}
# keys = ['key1', 'key2', 'key3', 'key4', 'key5']
# def_val = False
# dict = {key: False for key in range(5)}
# dict = {key: 'AAA' for key in range(5)}
#
# print(dict)


#  вариант 2
#
# for val in d:
#     if val in d.keys():
#         print(d[val], end='\n')
# print('\n')
# print(1 in d.values())
# print('1' in d.values())
# print('два' in d.values())
# print(1 in d.keys())
# print(d.values())