#	Кроме блокировок и примитивов синхронизации существует еще один способ обмена данными между потоками.
# Это очереди - Queue - https://docs.python.Org/3.6/library/queue.html
# В очередь можно положить элемент и взять его. Queue гарантирует что потоки не помешают друг другу
#	- операции очереди атомарные и блокирующие.
# логика процессов:  есть лодка, в  ней рыбаки, если рыбак поймал рыбу он передает ее приемщику
#  у приемщика 2 руки, одновременно он может взять только 2 рыбы, что бы положить садок поэтому
#  в стр. 47 класс Boat длина очереди Queue(maxsize=2)

import time
from collections import (defaultdict)

import queue
import random
import threading

fishes = (None, 'плотва', 'окунь', 'лещ')

# Посадим всех рыбаков в лодку, в которой есть садок для улова. 1 usage
class Fisher(threading.Thread):
    def __init__(self, name, worms, assistant, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.assistant = assistant

    def run(self):
        for worm in range(self.worms):
            print(f'{self.name}: забросил {worm} раз,  ждем...', flush=True)
            time.sleep(random.randint(5, 10) / 10)
            fish = random.choice(fishes)
        if fish is None:
            # print(f'{self.name}, {worm}: сожрали червяка!', flush=True)
            print(f'{self.name}: сожрали червяка!', flush=True)
        else:
            # print(f'{self.name}, {worm}: поймал {fish} и хочет положить его в садок', flush=True)
            print(f'{self.name}: поймал {fish} и хочет положить его в садок', flush=True)
            if self.assistant.full():  # проверяем - может приемщик взять рыбу у рыбака и положить в садок?
                # print(f'{self.name}, {worm}: приемщик занят !!!', flush=True)
                print(f'{self.name}: приемщик занят !!!', flush=True)
            # Этот метод у очереди - атомарный и блокирующий
            # Поток приостанавливается, пока нет места в очереди
            self.assistant.put(fish)
            print(f'{self.name}, {worm}: наконец-то отдал  {fish} приемщику\n', flush=True)

class Boat(threading.Thread):
    def __init__(self, worms_per_fisher = 10, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fishers = []
        self.worms_per_fisher = worms_per_fisher

        self.assistant = queue.Queue(maxsize=2)   # приемщик рыбы от рыбаков, кладет ее в общий садок
        #  у приемщика 2 руки, одновременно он может взять только 2 рыбы, что бы положить садок поэтому
        #  длина очереди Queue(maxsize=2)

        self.fish_tank = defaultdict(int)   # общий садок для всех рыбаков

    def add_fisher(self, name):
        fisher = Fisher(name = name, worms = self.worms_per_fisher, assistant = self.assistant)
        self.fishers.append(fisher)

    def run(self):
        print('Лодка вышла в море...', flush=True)
        for fisher in self.fishers:     # старт процесса рыбалки (Fisher, run) для всех рыбаков в лодке
            fisher. start()
        while True:
            try:
                # Этот метод у очереди - атомарный и блокирующий,
                # Поток приостанавливается, пока нет элементов в очереди
                fish = self.assistant.get(timeout=2)
                print(f'Приемщик принял {fish} и положил в садок', flush=True)
                self.fish_tank[fish] += 1
            except queue.Empty:
                print(f' Приемщик бездельничает в течении 1 секунды', flush=True)
                if not any(fisher.is_alive() for fisher in self.fishers):
                    break
            for fisher in self.fishers:
                fisher.join()
            print(f'Лодка возвращается домой c {self.assistant}', flush=True)

boat = Boat( worms_per_fisher = 10)
humans = ['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава', ]
for name in humans:
    boat.add_fisher(name = name)

boat.start()
boat.join()

print(f'лодка привезла {boat.fish_tank}')

#	Мы использовали очередь вида FIFO - first input, first output - первый вошел, первый вышел.
# В модуле queue есть еще два вида очередей:
#	LifoQueue - last input, first output - последний вошел, первый вышел (еще такую очередь называют стеком).
#	PriorityQueue - первым возвращается наименьший элемент, то есть sorted(list(entries))[0]
