import threading
import time
from threading import Thread
lock = threading.Lock()

class BankAccount(Thread):
    def __init__(self, account = 1000, amount = 0):
        Thread.__init__(self)
        self.account = account
        self.amount = amount
        self.account_lock = lock


    def deposit_task(self, account, amount):
        self.account_lock.acquire()
        self.account += amount
        self.account_lock.release()
        print(f'Вклад {amount}, баланс счета {account}')
        time.sleep(1)

    def withdraw_task(self, account, amount):
        self.account_lock.acquire()
        self.account -= amount
        self.account_lock.release()
        print(f'снято со счета  {amount}, баланс счета {account}')
        time.sleep(0.8)

    def run(self):
       if self.amount > 0:
           for _ in range(5):
               self.deposit_task(self.account, self.amount)
       else:
           for _ in range(5):
               self.withdraw_task(self.account, self.amount)




parent = BankAccount(amount = 100)
сhild = BankAccount(amount := -150)

parent.start()
сhild.start()

parent.join()
сhild.join()
