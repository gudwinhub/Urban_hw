def test_func():
    def inner_func():
        print('Я в области видимости функции test_function')

    print('я test_func')
    inner_func()


test_func()
inner_func()
