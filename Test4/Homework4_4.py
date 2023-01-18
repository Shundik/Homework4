import time
from datetime import datetime

n = int(input('Количество до 5 :'))
t = [datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')]
time.sleep(1)
t_1 = [datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')]
time.sleep(1)
t_2 = [datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')]
time.sleep(1)
t_3 = [datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')]
time.sleep(1)
t_4 = [datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')]


def simple():
    for i in t:
        if n == 1:
            yield [i]
        if n == 2:
            time.sleep(1)
            yield [i] + t_1
        if n == 3:
            yield [i] + t_1 + t_2
        if n == 4:
            yield [i] + t_1 + t_2 + t_3
        if n == 5:
            yield [i] + t_1 + t_2 + t_3 + t_4


for i in simple():
    print(i)
