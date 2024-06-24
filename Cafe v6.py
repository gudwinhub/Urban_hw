import queue
import threading
import time
import random
from threading import Thread
from time import sleep
from queue import Queue

global queue_visitor

class Cafe(Thread):

    def __init__(self, amount_tables = 3, *args):  # table_free = True
        super().__init__(*args)
        self.amount_tables = amount_tables
        # self.queue_visitor = queue.Queue()  # queue.Queue(maxsize= )
        self.tables = Table(amount_tables)
        self.lock = threading.Lock()
        # self.visitors = []
        
    # def visitor_arrival(self, name_visitor):
    #     visitor = Visitor(name_visitor, self.queue_visitor)
    #     self.visitors.append(visitor)

    def visitor_served(self, visitor):
        self.num_busy_table = self.Table.get_free_table()
        if self.num_busy_table != 0:  # если есть свободные столики (хотя бы один)
            with lock:
                Table.set_param(num_table = self.num_busy_table, is_busy = True) # меняем статус столика на Занято
                print(f'{visitor} занял столик № {self.num_busy_table})')
                time.sleep(random.randint(4, 7))  # время обслуживания
                Table.set_param(num_table = self.num_busy_table, is_busy = False)
                print(f'Посетитель {visitor} поел и пошел ...ь')
        else:
            print(f'К сожалению свободных столиков нет! совсем нет! ...посетитель {visitor} ждет...')

    def __run__(self):
        # queue_visitor.get(k)
        while not queue_visitor.empy():
            num_vistr = queue_visitor.get(k)
            visitor_served(num_vistr)
        

# ------------------------------------------------------------------------------
# Клас Table  - генерит список свободных столов
class Table:
    # паттерн Singleton - что бы объект класса Table был всегда только в одном экземпляре
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self, num_table):
        self.num_table = num_table
        self.is_busy = False        #  is_busy = False  - столик не занят
        self.tables = {key: False for key in range(1, num_table+1)} # генерим свободные столики
        print(self.tables)
    def get_free_table(self):    # получить номер свободного столика
        # условие поиска: False in tables.values() - если стол свободен результат = True
        for num_free_table, value in self.tables.items(): # проходимся по словарю со столиками {key: value,  ,  }
            if value == False:  # если value ключа = False
                return num_free_table  # возвращаем  key(значение)
            else:
                return 0

    def get_param(self):
        return self.num_table, self.busy
    
    def set_param(self, num_table, is_busy = False):
    # вызов с параметром только номер стола устанавливает статус стола - свободен
    #     self.num_table = num_table
    #     self.is_busy = is_busy
        self.tables[num_table] = is_busy
        
#----------------------------------------------------

# Класс Посетитель - генерит поток желающих поесть
class Visitor(Thread):  # класс Посетитель - гененрирует независимый поток голодных посетителей :-)
    def __init__(self, amount_visitors = 20, * args):  # name, queue_visitor
        super().__init__(*args)
        self.amount_vistrs = amount_visitors
        self.lock = threading.Lock()

    def thr_visitor(self):
        for k in range(1, self.amount_vistrs + 1):
            try:
                self.lock.acquire()
                print('поток посетителей  получил блокировку')
                queue_visitor.put(k)
                print(f'Посетитель {k} желает отобедать занимает очередь в кафе')
            finally:
                self.lock.release()
            time.sleep(random.randint(1, 2)) # интервал между посетителями 1-2 сек


cafe = Cafe(5) # задаем количество столиков в кафе (по умолчанию = 3)
visitors = Visitor(30) # задаем размер оока посетителей (по умолчанию = 20


visitors.start(25)
cafe.start()

visitors.join()
cafe.join(timeout = 2)