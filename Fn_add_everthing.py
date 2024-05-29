def add_everthing_up(a, b):
    try:
        result = a + b
    except TypeError:
        if type(a) != isinstance(int, float) or type(b) != isinstance(int, float): # если один из параметров не число
            result = str(a) + str(b) # преобразовываем в текст и применяем конкатенацию
    finally:
        return result

print(add_everthing_up(1, 3.5))
print(add_everthing_up(1, 'строка'))
print(add_everthing_up('строка1 ', 'строка2'))
print(add_everthing_up('строка', True))
print(add_everthing_up(False, True)) # с точки зрения логики True это 1, False - 0
print(add_everthing_up(1, True))