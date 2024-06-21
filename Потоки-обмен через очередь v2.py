# from collections import defaultdict
# a = defaultdict(int)
# a[1] = 1
# a[2] = 2
#
# print(a)
# print(a.values())
# -----------------------------

import time
import queue
import random
import threading
from threading import Thread

global q
q = queue.Queue()

class ClassA():  # Thread
    # global q
    def __init__(self, *args):
        super().__init__(*args)
        self.lock = threading.Lock()
        self.var = 0

    def method_A(self):
        for _ in range(15):
            self.var += 1
            # print(f'преременную {self.var}, запихуем в очередь')
            # self.lock.acquire()
            try:
                print('поток класса А - получил блокировку')
                print(f'преременную {self.var}, запихуем в очередь')
                q.put(self.var)
            finally:
                print()
                # self.lock.release()
            time.sleep(0.7)

class ClassB():

    def __init__(self,*args):
        super().__init__(*args)
        self.lock = threading.Lock()
        self.var = 20

    def method_B(self):
        for _ in range(15):
            self.var += 1
            self.lock.acquire()
            print('поток класса B  - получил блокировку')
            try:
                print(f'преременную {self.var}, запихуем в очередь')
                q.put(self.var)
            finally:
                self.lock.release()
                print()
            time.sleep(1)


class ClassC(): # выбираем данные из очереди Thread

    def __init__(self,*args):
        super().__init__(*args)
        # self.lock = threading.Lock()

    def method_C(self):
        for _ in range(30):
            # self.lock.acquire()
            try:
                print(f'изъяли из очереди', q.get())
            finally:
                # self.lock.release()
                print()
            time.sleep(0.5)

obj1 = ClassA()
obj2 = ClassB()
obj3 = ClassC()
th1 = threading.Thread(target=obj1.method_A)
th2 = threading.Thread(target=obj2.method_B)
th3 = threading.Thread(target=obj3.method_C)
th1.start()
th2.start()
th3.start()

th1.join()
th2.join()
th3.join()

while not q.empty():
    print(q.get(), end=' ')

#  Резюме - если 2 и более потока выполняют одинаковые операции put()/ ge() нужна блокировка очереди
#  если операции разные, один поток - put(), другой - get(), то для очереди типа FIFO  блокировка не нужна!