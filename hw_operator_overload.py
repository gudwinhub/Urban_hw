class Building:
    def __init__(self, numfloors=1, bldType='undef'):
        self.numfloors = numfloors
        self.bldType = bldType
        print('Тип здания - ', self.bldType, '\nколичество этажей в доме по умолчанию - ', self.numfloors)

    def __eq__(self, other):
        return self.numfloors == other.numfloors and self.bldType == other.bldType

        # def setnumfl(self, floors):
    #     self.numfloors = floors


home1 = Building(3, 'каменный')
home2 = Building(2, 'каменный')
if home1 == home2:
    print('строения похожи')
else:
    print('строения разные')
