class Building:
    def __init__(self, numfloors=1, bldType='undef'):
        self.numfloors = numfloors
        self.bldType = bldType
        print('Тип здания - ', self.bldType, '\nколичество этажей в доме по умолчанию - ', self.numfloors)

    def __eq__(self, other):
        if self.numfloors == other.numfloors and self.bldType == other.bldType:
            result = 'строения похожие'
        else:
            result = 'строения отличаются'
        return result

        # def setnumfl(self, floors):
    #     self.numfloors = floors


home1 = Building(2, 'каменный')
home2 = Building(2, 'каменный')
if home1 == home2:
    print()
