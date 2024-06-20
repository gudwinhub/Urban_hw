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

class ClassA(Thread):
    # global q
    def __init__(self, *args):
        super().__init__(*args)
        self.lock = threading.Lock()
        self.var = 0

    def method_A(self):
        for _ in range(15):
            self.var += 1
            print(f'преременную {self.var}, запихуем в очередь')
            self.lock.acquire()
            try:
                print('поток класса А - получил блокировку')
                q.put(self.var)
            finally:
                self.lock.release()
            time.sleep(1)

class ClassB(Thread):
    # global q
    def __init__(self,*args):
        super().__init__(*args)
        self.lock = threading.Lock()
        self.var = 20

    def method_B(self):
        for _ in range(15):
            self.var += 1
            print(f'преременную {self.var}, запихуем в очередь')
            self.lock.acquire()
            try:
                print('поток класса B  - получил блокировку')
                q.put(self.var)
            finally:
                self.lock.release()
            time.sleep(0.7)

obj1 = ClassA()
obj2 = ClassB()

th1 = threading.Thread(target=obj1.method_A)
th2 = threading.Thread(target=obj2.method_B)
th1.start()
th2.start()

th1.join()
th2.join()

while not q.empty():
    print(q.get(), end=' ')
