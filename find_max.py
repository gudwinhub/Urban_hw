def find_max(*args):
    n = len(args)
    if not args:
        return (print('вы забыли ввести числа'))
    elif n == 1:
        # return(max_num = args[n-1])
        return (args[0])
    elif n > 1:
        n -= 1
        max_num = args[n]
        num_tmp = args[n - 1]
        print(max_num, num_tmp)
        # find_max(*args[:n])

    if max_num > num_tmp:
        args[n-1] = max_num
        find_max(*args[:n])


    # max_num = num_tmp
    # find_max(args[:n-1])
    # return max_num


print(*find_max(11, 47, 35, 25))
