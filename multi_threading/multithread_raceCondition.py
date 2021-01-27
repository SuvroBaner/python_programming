# ----------------- Thread synchronization in case of Multithreading in Python ------------------
# It is a mechanism which ensures that two or more concurrent threads do not simultaneously execute some particular
# program segment known as critical section (shared resources)

# Race Condition : A race condition occurs when two or more threads can access shared data and they try to
# change it at the same time. As a result, the values of variables may be unpredictable and vary depending on
# the timings of context switches of the processes.

# The below code explains a race condition -

import threading

x = 0 # global variable

def increment():
    global x
    x += 1 # increment global variable x

def thread_task():
    for _ in range(100000):
        increment()

def main_task():
    global x
    x = 0

    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == '__main__':
    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i, x))

# Here, the expected result is 200000. But you can see that in some of the iteration it is a garbage value
# this is due to race condition.
# So, we need to properly synchronize between multiple threads using Locks