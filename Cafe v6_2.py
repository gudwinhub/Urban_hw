import queue
import threading
import time
import random
from threading import Thread
from time import sleep
from queue import Queue

global queue_visitor
queue_visitor = Queue()
class Cafe(Thread):

    def __init__(self, amount_tables = 3, *args, **kwargs):  # table_free = True
        super().__init__(*args, **kwargs)
        # tables = Table(amount_tables)
        self.tables = Table(amount_tables)
        self.amount_tables = amount_tables

        self.lock = threading.Lock()
        # self.queue_visitor = Queue()  # queue.Queue(maxsize= )

    # def visitor_arrival(self, name_visitor):
    #     visitor = Visitor(name_visitor, self.queue_visitor)
    #     self.visitors.append(visitor)

    def visitor_served(self, visitor):
        # self.num_busy_table = Table.get_free_table()
        self.num_busy_table = self.tables.get_free_table()
        if self.num_busy_table != 0:  # если есть свободные столики (хотя бы один)
            with self.lock:
                self.tables.set_param(num_table = self.num_busy_table, is_busy = True) # меняем статус столика на Занято
                print(f'{visitor} занял столик № {self.num_busy_table})')
                time.sleep(random.randint(4, 7))  # время обслуживания
                self.tables.set_param(num_table = self.num_busy_table, is_busy = False)
                print(f'Посетитель {visitor} поел и пошел ...ь')
        else:
            print(f'К сожалению свободных столиков нет! совсем нет! ...посетитель {visitor} ждет...')

    def run(self):
        # queue_visitor.get(k)
        # visitors = Visitor()  # задаем размер оока посетителей (по умолчанию = 20
        # visitors_arrival_thread = threading.Thread(target=visitors.thr_visitor)
        # visitors_arrival_thread.start()

        if queue_visitor.empty():
            time.sleep(2)
        else:
            while not queue_visitor.empty():
                # visitors_arrival_thread.join()
                with self.lock:
                    num_vistr = queue_visitor.get()
                    Cafe.visitor_served(num_vistr)
        

# ------------------------------------------------------------------------------
# Клас Table  - генерит список свободных столов
class Table:
    # паттерн Singleton - что бы объект класса Table был всегда только в одном экземпляре
    # __instance = None
    # def __new__(cls):
    #     if cls.__instance is None:
    #         cls.__instance = super().__new__(cls)
    #     return cls.__instance
    
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
    def __init__(self, amount_visitors = 10, *args, **kwargs):  # name, queue_visitor
        super().__init__(*args, **kwargs)
        self.amount_vistrs = amount_visitors
        self.lock = threading.Lock()

    def run(self):  #thr_visitor(self)
        for k in range(1, self.amount_vistrs + 1):
            with self.lock:
                print('поток посетителей  получил блокировку')
                queue_visitor.put(k)
                print(f'в очереди {queue_visitor.qsize()}')
                print(f'Посетитель {k} желает отобедать занимает очередь в кафе')
            #     self.lock.acquire()
            #     print('поток посетителей  получил блокировку')
            #     queue_visitor.put(k)
            #     print(f'Посетитель {k} желает отобедать занимает очередь в кафе')
            # finally:
            #     self.lock.release()
            time.sleep(random.randint(1, 2)) # интервал между посетителями 1-2 сек


cafe = Cafe(5) # задаем количество столиков в кафе (по умолчанию = 3)
cafe.start()
cafe.join()

visitors = Visitor() # задаем размер оока посетителей (по умолчанию = 20
visitors.start()
visitors.join()
print(queue_visitor.get())

# visitors_arrival_thread = threading.Thread(target=visitors.thr_visitor)
# visitors_arrival_thread.start()
# visitors_arrival_thread.join()
