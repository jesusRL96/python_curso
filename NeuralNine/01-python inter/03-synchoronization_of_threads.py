import threading
import time

x = 8192
# used to lock a resourse until it's free
# it'll be lock when lock.acquire() and free until lock.release
lock = threading.Lock()


def double():
    global x, lock
    lock.acquire()
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("reached the maximum")
    lock.release()

def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("reached the minimum")
    lock.release()
# the first thread will be the one execute, and the thread 2 won't be execute until te first be released
# t1 = threading.Thread(target=halve)
# t2 = threading.Thread(target=double)
# t1.start()
# t2.start()
# ================================================================
# values defines the maximum number of access
# it allows 5 threads to have access to the target function
# the other threads wont have access until one release
semaphore = threading.BoundedSemaphore(value=5)

def access(thread_number):
    print(f"{thread_number} is trying to access")
    semaphore.acquire()
    print(f"{thread_number} was granted access")
    time.sleep(10)
    print(f"{thread_number} is releasing")
    semaphore.release()

for thread_number in range(1,11):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
    time.sleep(1)