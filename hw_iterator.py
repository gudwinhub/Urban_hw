2
class EvenNumbers:
    def __init__(self, max):
        self.max = max
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num & gt;= self.max:
            raise StopIteration
        else:
            self.num += 2
            return self.num - 2