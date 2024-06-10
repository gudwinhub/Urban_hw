import threading
import time
from threading import Thread

def num_prn():
    for i in  range(11):
        print(i)
        time.sleep(1)


def chr_prn():
    for i in range(97, 107):
        print(chr(i))
        time.sleep(1)


th_num = Thread(target=num_prn, args=())
th_chr = Thread(target=chr_prn, args=())
th_num.start()
th_num.join(0.5)
th_chr.start()




