
n = int(input('введите число элементов ряда Фибоначчи -> '))

# вариант 1
fib1 = 0
fib2 = 1
print('вариант', sep='')
print(fib1,fib2, sep=' ', end=' ')
i = 0
while i < n-2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
    print(fib2, end=' ')

# вариант 2
# более компактный, но не такой наглядный

fib1 = 0
fib2 = 1
print('\n'*2, 'вариант 2 \n', sep='')
print(fib1, fib2, sep=' ', end=' ')

while (n-2) > 0:
    fib1, fib2 = fib2, fib1 + fib2
    n -= 1
    print(fib2, end=' ')

# вариант 3
# с использование цикла for
#
fib1 = 0
fib2 = 1

print('\n'*2, 'вариант 3 \n', sep='' )
print(fib1, fib2, sep=' ', end=' ')

for i in range(1, n+2):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

#  ньюанс  решений выше - числа ряда Фибоначи только печатаются и не сохраняются
#  если необхомино сохранить применяем более другое решение
# создаем переменную типа Список и в него добавляем все числа
# или вариант 4 - вычисление нужного числа через функцию рекурсии

 # вариант 4
 # рекурсивное вычисление элементов ряда Фибоначи

def fibonachi(n):
    # print(n)
    if n == 1 or n == 2:
        # print('if n= ', n)
        return 1
    return fibonachi(n - 1) + fibonachi(n - 2)

n = int(input('\n введите номер элемента ряда Фибоначчи -> '))
print('число Фибоначи через рекурсию ', fibonachi(n-1) )


