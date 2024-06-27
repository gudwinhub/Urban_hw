# from collections import defaultdict
# a = defaultdict(int)
# a[1] = 1
# a[2] = 2
#
# print(a)
# print(a.values())
# -----------------------------
import logging
import time
import queue
import random
import threading
from threading import Thread

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s', )
global q
q = queue.Queue()

class ClassA(Thread):  # Thread
    # global q
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lock = threading.Lock()
        self.var = 0

    def run(self):
        for _ in range(15):
            self.var += 1
            # print(f'преременную {self.var}, запихуем в очередь')
            # self.lock.acquire()
            try:
                # print('поток класса А - получил блокировку')
                print(f'преременную {self.var}, запихуем в очередь')
                q.put(self.var)
            finally:
                print()
                # self.lock.release()
            time.sleep(0.7)

class ClassB(Thread):

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lock = threading.Lock()
        self.var = 20

    def run(self):
        for _ in range(15):
            self.var += 1
            self.lock.acquire()
            # print('поток класса B  - получил блокировку')
            try:
                print(f'преременную {self.var}, запихуем в очередь')
                q.put(self.var)
            finally:
                self.lock.release()
                print()
            time.sleep(1)


class ClassC(Thread): # выбираем данные из очереди Thread

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lock = threading.Lock()

    # def method_C(self):
    def run(self):
        for _ in range(30):
            self.lock.acquire()
            try:
                print(f'изъяли из очереди', q.get())
            finally:
                self.lock.release()
                print()
            time.sleep(0.5)

th1 = ClassA()
th2 = ClassB()
th3 = ClassC()

th1.start()
th2.start()
th3.start()

th1.join()
th2.join()
th3.join()

# th1 = threading.Thread(target=obj1, )
# th2 = threading.Thread(target=obj2)
# th3 = threading.Thread(target=obj3)
# th1.start()
# th2.start()
# th3.start()

# th1.join()
# th2.join()
# th3.join()

while not q.empty():
    print(q.get(), end=' ')

#  Резюме - если 2 и более потока выполняют одинаковые операции put()/ ge() нужна блокировка очереди
#  если операции разные, один поток - put(), другой - get(), то для очереди типа FIFO  блокировка не нужна!