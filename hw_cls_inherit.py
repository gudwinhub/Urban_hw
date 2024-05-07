class Car():
    price = 1000000
    engine_pw = 100
    engine_type = 'gas'
    car_type = 'седан'

    def __init__(self):
        pass

    def hours_pw(self):
        return self.engine_pw

class Nissan(Car):
    price = 1500000
    # def __init__(self, price = 1500000): # это для экземпляра класса
    #     self.price = price

    def hours_pw(self, engine_pw):
        self.engine_pw = engine_pw

class Kia(Car):
    def __init__(self, price = 1700000):
        self.price = price

    def hours_pw(self, engine_pw):
        self.engine_pw = engine_pw

car = Car()
print('базовая цена авто ', car.price, 'мощность двигателя', car.hours_pw())

nissan = Nissan()
print('Nissan (price) ', nissan.price, 'мощность двигателя: ', nissan.engine_pw)
nissan.price = 1900000
nissan.hours_pw(150)
print('Nissan (price) ', nissan.price, 'мощность двигателя: ', nissan.engine_pw)


kia = Kia()
print('KIA (price) ', kia.price, 'мощность двигателя: ', kia.engine_pw)
kia = Kia(2000000)
kia.hours_pw(160)
print('KIA (price) ', kia.price, 'мощность двигателя: ', kia.engine_pw)