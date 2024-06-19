import queue
from threading import Thread
from time import sleep
from queue import Queue

class Cafe(Thread):

    def __init__(self, amount_tables, amount_visitor = 20, *args):  # table_free = True
        super().__init__(*args)
        self.amount_tables = amount_tables
        self.amount_visitor =amount_visitor
        self.queue_visitor = queue.Queue()  # queue.Queue(maxsize= )
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
        print('запуск потока customer_arrival_thread.start()')
        customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
        customer_arrival_thread.start()
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
#-------------------------------------------------------
class Visitor(Thread):
    def __init__(self, name, queue_visitor):
        self.name = 'Посетитель ' + str(name)
        self.queue_visitor = queue_visitor
    def __run__(self):
        self.queue_visitor.put(self.name) # Посетитель N занял очередь в кафе


cafe = Cafe(5)