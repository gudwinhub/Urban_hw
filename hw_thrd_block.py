import threading
import time
from threading import Thread


class BankAccount(Thread):

    def __init__(self, amount, lock): # account,
        Thread.__init__(self)
        self.amount = amount
        self.account_lock = lock


    def deposit_task(self, amount, lock):  # account,
        global total_account
        self.account_lock.acquire()
        total_account += amount
        print(f'Вклад {self.amount}, баланс счета {total_account}')
        self.account_lock.release()
        time.sleep(1)

    def withdraw_task(self,amount, lock):   # account,
        global total_account
        self.account_lock.acquire()
        total_account += amount
        print(f'снято со счета  {self.amount}, баланс счета {total_account}')
        self.account_lock.release()

        time.sleep(0.8)

    def run(self):
       global total_account
       if self.amount > 0:
           for _ in range(5):
               self.deposit_task(self.amount, self.account_lock)  # self.account,
       else:
           for _ in range(5):
               self.withdraw_task(self.amount, self.account_lock) # self.account,


lock = threading.Lock()
total_account = 1000
parent = BankAccount(amount = 100, lock = lock)  # account = total_account,
сhild = BankAccount(amount = -150, lock = lock)  # account = total_account,

parent.start()
сhild.start()

parent.join()
сhild.join()
print(f'Итого средств на счете {total_account}')