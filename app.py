from philosopher import Philosopher
import threading

forks = []
philosophers = []

for i in range(5):
    f = threading.BoundedSemaphore(1)
    forks.append(f)

for i in range(5):
    p = Philosopher(i, forks)
    p.start()
    philosophers.append(p)

for i in philosophers:
    i.join()