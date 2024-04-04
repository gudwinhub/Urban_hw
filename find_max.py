def find_max(*args):
    num_tmp = 0
    # global num_tmp
    n = len(args)
    if not args:
        return (print('вы забыли ввести числа'))
    elif n == 1:
        num_tmp = args[0]
        return num_tmp
    else:
        n -= 1
        max_num = args[n]
        # num_tmp = args[n - 1]
        # print(type(max_num), type(num_tmp), type(args), sep = ' ')
        args = list(args)
        num_tmp = find_max(*args[:n])
        if max_num < num_tmp:
            max_num = num_tmp
            # print(max_num)
        return max_num
# вызов с заданием аргументов в теле вызова
print(find_max(11, 47, 35, 89, 58, 33,78,24,78))

# вызов с заданием аргументов через список
lst = [56, 23, 45, 78, 89, 56, 23, 45, 78, 92, 56, 23, 45, 78, 92]
print(find_max(*lst))