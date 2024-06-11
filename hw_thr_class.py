import time
from threading import Thread

class Knights(Thread):
    def __init__(self, name, skill, enemies = 100, *args):
        super(Knights, self).__init__(*args)
        self.name = name
        self.skill = skill
        self.enemies = enemies
        self.dob = 0    # days of battle - сколько дней длится битва
    def run(self):
        print(f"{self.name} на нас напали!\n")
        while self.enemies > 0:
            self.enemies -= self.skill
            self.dob += 1
            print(f"{self.name}  бъется ужо {self.dob} день\дня\дней...осталось добить {self.enemies} врагов")
            time.sleep(1)
        print('\n'*2, f"{self.name} героически бился насмерь {self.dob} дней!!! \n ")


khight1 = Knights('Khight1', 10)
khight2 = Knights('Knaghts2', 20)
print('начало битвы')

khight1.start()
khight2.start()
#
khight1.join()
khight2.join()
