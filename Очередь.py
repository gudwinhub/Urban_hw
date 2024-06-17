from threading import Thread
from time import sleep
import queue
from queue import Queue

q = queue.Queue(2)
class Cafe:     # (Thread)

	def __init__(self, num_tables, *args):  # table_free = True
		super().__init__(*args)
		# self.queue_visitor = 0  # очередь посетителей в кафе
		# self.tables = tables
		self.tables = dict([Table(i+1).get_param() for i in range(num_tables)])
		# self.amount_tables = len(tables)    # количество столиков в кафе
		# self.table_free = queue.Queue(maxsize= amount_table)    # очередь - свободные столики
		self.queue_visitor = queue.Queue() # maxsize= amount_table)
		print(self.tables)

class Table:
	# __instance = None
	#
	# def __new__(cls, *args, **kwargs):
	# 	if cls.__instance is None:
	# 		cls.__instance = super().__new__(cls)
	# 	return cls.__instance

	def __init__(self, num_table, is_busy = False):
		self.num_table = num_table
		self.busy = is_busy

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

cafe = Cafe(3)

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