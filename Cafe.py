# Моделирование работы сети кафе с несколькими столиками и потоком посетителей,
# прибывающих для заказа пищи и уходящих после завершения приема.
# Есть сеть кафе с несколькими столиками. Посетители приходят, заказывают еду, занимают столик, употребляют еду и уходят.
# Если столик свободен, новый посетитель принимается к обслуживанию, иначе он становится в очередь на ожидание.

import time
import queue
import random
import threading
from threading import Thread

# клас Кафе
class Cafe(Thread):

    def __init__(self, tables, *args):  # table_free = True
        super().__init__(*args)
        # self.queue_visitor = 0  # очередь посетителей в кафе
        self.tables = dict([Table(i + 1).get_param() for i in range(num_tables)])
        # self.amount_tables = len(tables)    # количество столиков в кафе
        # self.table_free = queue.Queue(maxsize= amount_table)    # очередь - свободные столики
        self.queue_visitor = queue.Queue()  # maxsize= amount_table)
        print(self.tables)

    def visitor_arrival(self):
        for n in range(1, amount_visitor=1):
            self.visitor = 'Посетитель'+ str(n)
            print(f'Пришел посетитель {n}.')
            time.sleep(1)  # time.sleep(random.randint(1, 3))

    def visitor_served(self, visitor):
        if
        time.sleep(5)
        pass

    def run(self):

# -----------------------------------------------
# Класс столов
class Table():
    def __init__(self, num_table, is_busy=False):
        self.__num_table = num_table
        self.__busy = is_busy

    def get_busy(self):
        return [self.__num_table, self.__busy]

    def set_busy(self, is_busy):
        self.__busy = is_busy

    busy = property(get_busy, set_busy)
# -----------------------------------------
# класс   Посетитель
class Vistor(Thread):
    def __init__(self, name):
        super().__init__(*args)
        num_visitor = name

    def run(self):
        # время затраченное на прием пищи или сколько времени стол был занят посетителем
        mealtime = time.sleep(random.randint(1, 5))
        print(f'посетитель {name} занимал столик  {mealtime} мин. ')

# ---------------------------------------


# создаем 3 столика в кафе
tables = [Table(i+1) for i in range(3)]

# инициализируем класс Кафе
сafe = Cafe(amount_tables = tables)

# Запускаем поток для прибытия посетителей
visitor_arrival_thread = threading.Thread(target=cafe.visitorr_arrival, args=(10))
visitor_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
visitor_arrival_thread.join()
