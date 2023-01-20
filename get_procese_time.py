import time


def procese_time(func):
    t1 = time.time()
    func()
    print(time.time()-t1)


def f():
    n = []
    for i in range(1000000):
        n.append(i)


procese_time(f)
