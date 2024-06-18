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
        self.queue_visitor = Queue  # queue.Queue(maxsize= )
        self.tables = Table(amoun_table)

    def visitor_arrival(self):
        for n in range(1, amount_visitor=1):
            self.visitor = 'Посетитель'+ str(n)
            print(f'Пришел посетитель {n}.')
            time.sleep(1)  # time.sleep(random.randint(1, 3))

    def visitor_served(self, visitor):
        # условие поиска: False in tables.values() - если стол свободен результат = True
        self.num_free_table = self.tables.get_free_table()
        if self.num_free_table != 0:  # если есть свободные столики (хотя бы один)
            print(self.num_free_table)

        else:
            print(f'Все столики заняты, посетитель {n} ожидает свободный столик.')
            # self.queue_visitor.put(self.visitor)

    def run(self):

# -----------------------------------------------
# Класс столов
class Table():
    def __init__(self, amount_table, amount_visitor =20, *args):
        super().__init__(*args)
        self.amount_table = amount_table
        self.amount_tables = amount_tables
        self.amount_visitor = amount_visitor
        # self.is_busy = False  #  is_busy = False  - столик не занят
        self.tables = {key: False for key in range(1, self.amount_table + 1)}  # генерим свободные столики

        # print(self.tables)

    def get_free_table(self):    # получить номер свободного столика
        for num_free_table, value in self.tables.items(): # проходимся по словарю со столиками {key: value,  ,  }
            if value == False:  # если value ключа = False # столик не занят
                return num_free_table  # возвращаем значение key
            else:
                return 0

    def set_busy(self, num_table, is_busy): # функция устанавливает для столика статус - ЗАНЯТО
        self.num_table = num_table  # номер столика
        self.is_busy = is_busy       # состояние : False - не занят / True - занят
        self.tables[self.num_table] = self.is_busy



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
