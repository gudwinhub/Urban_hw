import threading
from threading import Thread
import time
from time import sleep

import queue
from queue import Queue
# q = queue.Queue(2)
class Cafe:     # (Thread)

    def __init__(self, amount_tables, amount_visitor = 20, *args):  # table_free = True
        super().__init__(*args)
        self.amount_tables = amount_tables
        self.amount_visitor =amount_visitor
        self.queue_visitor = Queue  # queue.Queue(maxsize= )
        self.tables = Table(amount_tables)

        # self.queue_visitor = 0  # очередь посетителей в кафе
        # self.tables = tables
        # self.tables = dict([Table(i + 1).get_param() for i in range(num_tables)])
        # self.tables = Table.tables_gen(num_tables)  #   ?????
        # self.amount_tables = len(tables)    # количество столиков в кафе
        # self.table_free = queue.Queue(maxsize= amount_table)    # очередь - свободные столики
        # print(list(self.tables.values())[1])
        # for i in range(len(self.tables)):
        #     print(list(self.tables.values())[i])

    def visitor_arrival(self):
       for n in range(1, self.amount_visitor+1):
            self.visitor = 'Посетитель ' + str(n)
            print(f'Пришел {self.visitor}.')
            time.sleep(1)  # time.sleep(random.randint(1, 3))

    def visitor_served(self, visitor):
        # условие поиска: False in tables.values() - если стол свободен результат = True
        self.num_free_table = self.tables.get_free_table()
        if self.num_free_table != 0:  # если есть свободные столики (хотя бы один)
            print(self.num_free_table)

        else:
            print(f'Все столики заняты, посетитель {n} ожидает свободный столик.')
            # self.queue_visitor.put(self.visitor)


        # for i in range(len(self.tables)):
        # 		list(self.tables.values())[i]

    # def __run__(self):


class Table:
    # __instance = None
    #
    # def __new__(cls, *args, **kwargs):
    # 	if cls.__instance is None:
    # 		cls.__instance = super().__new__(cls)
    # 	return cls.__instance
    def __init__(self, num_table):
        self.num_table = num_table
        self.is_busy = False        #  is_busy = False  - столик не занят
        self.tables = {key: False for key in range(1, num_table+1)} # генерим свободные столики
        print(self.tables)

    # def tables_gen(self, num_table):
    #     self.tables = dict([Table(i + 1).get_param() for i in range(num_tables)])

    def get_free_table(self):    # получить номер свободного столика
        for num_free_table, value in self.tables.items(): # проходимся по словарю со столиками {key: value,  ,  }
            if value == False:  # если value ключа = False
                return num_free_table  # возвращаем  key(значение)
            else:
                return 0

    def get_param(self):
        return self.num_table, self.busy
    # def __init__(self, num_table, is_busy=False):
    # 	self.__num_table = num_table
    # 	self.__busy = is_busy

    # def get_busy(self):
    # 	return [self.__num_table, self.__busy]
    #
    # def set_busy(self, is_busy):
    # 	self.__busy = is_busy

    # param = property(get_busy, set_busy)
# ------------------------

# class Visitor:



# tables = Table(5)
# print(tables.get_free_table())



cafe = Cafe(5)

print(cafe.visitor_served())


# num_tables =5
# tables = dict([Table(i+1).get_param() for i in range(num_tables)])
# print(list(tables.values()))
# tables[3] = True
# print(list(tables.values()))
# print(True in tables.values())
# tables = dict([Table(i+1).get_param() for i in range(3)])
# tables[2] = True
#
# print(tables)

# table1 = Table(1).get_param()
# print(table1)

# dict_sample = dict([table1])
# print(dict_sample)
# tables = [Table(i + 1) for i in range(3)]

#  {key: value for key, value in zip(keys, values)}

# tables = dict'Посетитель'+str(i+1): value for i, False in range(3)}

# print(dict(1,2))


# a = table[0].param
# print(tables[0].busy)
# print(table[0].param)
# print(table[0].param[1])
# table1.busy = True
# print(table.param[1])

# q.put(table[0])
# print(q.qsize())
# q.put(table[1])
# print(q.qsize())
# print(q.full())
# print(q.put(table[2]))