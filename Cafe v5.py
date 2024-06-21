import queue
import threading
import time
import random
from threading import Thread
from time import sleep
from queue import Queue

# global queue_visitor
class Cafe(Thread):

    def __init__(self, amount_tables = 3, *args):  # table_free = True
        super().__init__(*args)
        self.amount_tables = amount_tables
        self.queue_visitor = Queue()  # количество посетителей не ограничено
        self.tables = Table(amount_tables)
        self.queue_tables = Queue(amount_tables) # буфер (очердь) из свободных столов
        # self.visitors = []

    def visitor_arrival(self):  #, name_visitor
        self.visitors = Visitor(20, self.queue_visitor)
        # self.visitors.append(visitor)




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
class Table(Thread):

    def __init__(self, num_table, queue_table):
        self.num_table = num_table
        self.is_busy = False        #  is_busy = False  - столик не занят
        self.tables = {key: False for key in range(1, num_table+1)} # генерим свободные столики
        print(self.tables)
        for i in range(num_table):
            self.queue_tables.put(i)

#----------------------------------------------------
class Visitor(Thread):  # класс Посетитель - гененрирует независимый поток голодных посетителей :-)
    def __init__(self,amount_visitor = 20, queue_visitors, * args):  # name, queue_visitor
        super().__init__(*args)
        self.amount_visitor = amount_visitor
        self.lock = threading.Lock()
        self.queue_visitors =

    def thr_visitor(self):
        for k in range(1, self.amount_visitor + 1):
            self.lock.acquire(
            try:
                # print('поток посетителей  получил блокировку')
                queue_visitor.put(k)
                print(f'Посетитель {k} желает отобедать занимает очередь в кафе')
            finally:
                self.lock.release()
            time.sleep(random.randint(1, 2)) # интервал между посетителями 1-2 сек


cafe = Cafe(5) # задаем количество столиков в кафе (по умолчанию = 3)
