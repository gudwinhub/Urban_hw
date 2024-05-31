def create_opr(operation):
    print(operation)
    if operation == "+":
       def add(*args):
            return sum(args)
       return add
    elif operation == "-":
        def subtr(x, y):
            return x-y
        return subtr

add = create_opr("+")
print(add(1, 2, 3))
minus = create_opr("-")
print(minus(10,3))

# но если по феншую то это нужно реализовать через класс и каждую функцию как метод класса
# например вот  так
class Math():
    # a: float
    # b: float

    # def __init__(self, a, b):
    #     a: float
    #     b: float

    def add(self, a, b):
        result = a + b
        print(result) # или return result вместо печати

    def subtr(self, a, b):
        print(a - b)

    def solve(self, name: str, a, b):
        if hasattr(self, name) and callable(getattr(self, name)):
            func = getattr(self, name)
            func(a, b)

math = Math()
math.solve("add", 5, 7)