def is_prime(func):
    def wrapper(*args):
        sum = func(*args)
        for i in range(2, (sum // 2) + 1):  # мудрствовать не будем, пойдем простым, не самым быстрым, путем для определения простого числа
            if sum % i == 0:
                return 'непростое'  #False
        return 'простое'     #True
    return wrapper

@is_prime
def sum3(a, b, c):
    return a + b + c


result = sum3(13, 4, 14)
print(result)