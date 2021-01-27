# A thread is an entity within a process that can be scheduled for execution. Also, it is the smallest unit of
# processing that can be performed in an OS (Operating System).

# Multithreading is defined as the ability of a processor to execute multiple threads (subset of process) concurrently -
# Multitasking : It is done in a single core CPU where threads are used by context switching

# https://www.geeksforgeeks.org/multithreading-python-set-1/

import threading

def print_cube(num):
    print("Cube: {}".format(num*num*num))

def print_square(num):
    print('Square: {}'.format(num*num))

if __name__ == '__main__':
    # creating thread -
    t1 = threading.Thread(target=print_square, args = (10, )) # creating the object of thread class
    t2 = threading.Thread(target=print_cube, args = (10, )) # (functions to be executed by the thread, arguments)

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # Once the threads start, the current program (you can think of it like a main thread) also keeps on executing.
    # In order to stop execution of current program until a thread is complete, we use join method.

    # As a result, the current program will first wait for the completion of t1 and then t2.
    # Once, they are finished, the remaining statements of current program are executed.

    # Both threads completely executed
    print("Done")