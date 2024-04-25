class House:
    def __init__(self):
        self.numfloors: int = 10
        print('количество этажей в доме по умолчанию - ', self.numfloors)

    def setnumfl(self, floors):
        self.numfloors = floors

        #


home1 = House()
flrs = int(input('задать количество этажей доме -> '))
home1.setnumfl(flrs)
print('задано новое количество этажей', home1.numfloors)
