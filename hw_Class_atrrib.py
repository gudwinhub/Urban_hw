class Buiding():
    count = 0
    address = ''
    def __init__(self, addrs):
        self.address = addrs
        Buiding.count += 1
    def __str__(self):
        return self.address + str(Buiding.count)

for i in range(40):
    bld = Buiding('здание ')
    print(bld)
