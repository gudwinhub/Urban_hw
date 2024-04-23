class House:
    def __init__(self):
        self.name = self
        # self.numbersOffFloors = None


home1 = House()
home1.numbersOfFloors = 10
print('Всего этажей', home1.numbersOfFloors)
for i in range(1, home1.numbersOfFloors + 1):
    print('Текущий этаж - ', i)
