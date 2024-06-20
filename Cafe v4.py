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
        self.visitors = []

    def visitor_arrival(self, name_visitor):
        visitor = Visitor(name_visitor, self.queue_visitor)
        self.visitors.append(visitor)

    def visitor_served(self, visitor):
        # условие поиска: False in tables.values() - если стол свободен результат = True
        self.num_free_table = self.tables.get_free_table()
        if self.num_free_table != 0:  # если есть свободные столики (хотя бы один)
            print(self.num_free_table)

        else:
            print(f'Все столики заняты, посетитель {n} ожидает свободный столик.')

    def __run__(self):

        # queue_visitor.get(k)

# ------------------------------------------------------------------------------
class Table:

    def __init__(self, num_table):
        self.num_table = num_table
        self.is_busy = False        #  is_busy = False  - столик не занят
        self.tables = {key: False for key in range(1, num_table+1)} # генерим свободные столики
        print(self.tables)
    def get_free_table(self):    # получить номер свободного столика
        for num_free_table, value in self.tables.items(): # проходимся по словарю со столиками {key: value,  ,  }
            if value == False:  # если value ключа = False
                return num_free_table  # возвращаем  key(значение)
            else:
                return 0

    def get_param(self):
        return self.num_table, self.busy
#----------------------------------------------------
class Visitor(Thread):  # класс Посетитель - гененрирует независимый поток голодных посетителей :-)
    def __init__(self,amount_visitor = 20, * args):  # name, queue_visitor
        super().__init__(*args)
        self.amount_visitor = amount_visitor
        self.lock = threading.Lock()

    def thr_visitor(self):
        for k in range(1, self.amount_visitor + 1):
            self.lock.acquire()
            try:
                # print('поток посетителей  получил блокировку')
                queue_visitor.put(k)
                print(f'Посетитель {k} желает отобедать занимает очередь в кафе')
            finally:
                self.lock.release()
            time.sleep(random.randint(1, 2)) # интервал между посетителями 1-2 сек


cafe = Cafe(5) # задаем количество столиков в кафе (по умолчанию = 3)
visitors = Visitor(30) # задаем размер оока посетителей (по умолчанию = 20