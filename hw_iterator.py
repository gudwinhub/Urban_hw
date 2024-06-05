class EvenNumbers(object):
    def __init__(self,min, max):
        self.max = max
        if min % 2 != 0:
            self.current = min + 1
        else:
            self.current = min

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max:
            raise StopIteration
        else:
            self.current += 2
            return self.current - 2

evnt_num = EvenNumbers(1, 15)

print(list(evnt_num))
