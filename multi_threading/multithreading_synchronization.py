# Synchronization of multiple threads to avoid race condition-

# Threading module provides a Lock class to deal with race conditions. Lock is implemented by using a
# Semaphore object provided by the OS.

# A semaphore is a synchronization object that controls access by multiple processes / threads to common resource
# in a parallel programming environment. It is simply a value in a designated place in the operating system (or kernel)
# storage that each process/thread can check and then change. It can be binary (0 or 1) or can have additional values.

import threading

x = 0 # global variable

def increment():
    global x
    x += 1

def thread_task(lock):
    for _ in range(100000):
        # In the critical section of target function, we apply lock using lock.acquire() method
        #  As soon as a lock is acquired, no other thread can access the critical section (here, increment function)
        #  until the lock is released using lock.release() method.
        lock.acquire() # To acquire a lock. A lock can be blocking or non-blocking.
        increment()
        lock.release() # To release a lock

def main_task():
    global x
    x = 0

    # creating a lock
    lock = threading.Lock()

    # creating threads
    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))

    # start threads
    t1.start()
    t2.start()

    # wait until threads finish their jobs
    t1.join()
    t2.join()

if __name__ == "__main__":
    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i, x))

# Here, the final value of x comes out to be 200000 every time (expected result)