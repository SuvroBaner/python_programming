# Difference between Multithreading and Multiprocessing in Python

# Multithreading - It is a technique where multiple threads (a unit of execution within a process) are spawned by a
# process to do different tasks, at about the same time, just one after the other. This gives you the illusion that
# the threads are running parallel, but they are actually run in a concurrent manner. In Python the Global Interpreter
# Lock (GIL) prevents the threads from running simultaneously.

# Multiprocessing - It is a technique where parallelism in its truest form is achieved. Multiple processes are run
# across multiple CPU cores, which do not share the resources among them. Each processes can have many threads
# running in its own memory space. In Python, each process has its own instance of Python interpreter doing the job
# of executing the instructions.

import time, os
from threading import Thread, current_thread
from multiprocessing import Process, current_process

COUNT = 200000000
SLEEP = 10

def io_bound(sec):
    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name

    print(f"{pid} * {processName} * {threadName} ---> Start Sleeping ...")
    time.sleep(sec)
    print(f"{pid} * {processName} * {threadName} ----> Finished Sleeping ...")

def cpu_bound(n):
    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name

    print(f"{pid} * {processName} * {threadName} ----> Start Counting ...")

    while n > 0:
        n -= 1

    print(f"{pid} * {processName} * {threadName} ----> Finished Counting ...")

def ispal(x):
    leftIdx = 0
    rightIdx = len(x) - 1
    while leftIdx < rightIdx:
        if x[leftIdx] != x[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True

if __name__ == '__main__':
    start = time.time()

    #st = 'madam'
    #print("The string {st} is palindrome : ", ispal(st))
    # Part-1
    # Here the main process calls our function twice one after the other using its default thread, Main Thread.
    #io_bound(SLEEP)
    #io_bound(SLEEP)

    # Part -2
    # Lets use threading in Python to speed up the execution of the functions. Both the threads (thread-1 and thread-2)
    # are started by our Main Process, each of which calls our function, at almost the same time. Both the threads
    # complete their job of sleeping for 10 secs concurrently. This reduced the total execution time of our whole
    # program by a significant 50%. Hence, multi-threading is the go-to solution for executing tasks wherein the idle
    # time of our CPU can be utilized to perform the other tasks. Hence, saving time by making use of the wait time.

    '''t1 = Thread(target = io_bound, args = (SLEEP, ))
    t2 = Thread(target = io_bound, args = (SLEEP, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()'''

    # Part - 3
    # Running the CPU - bound task twice, one after the other-
    # Note that it is once again our MainProcess calling the function twice, one after the other,
    # in its default thread, MainThread. Each execution of the whole program took 8 secs. So, total 16 secs.
    # Note here it is a CPU bound task.
    #cpu_bound(COUNT)
    #cpu_bound(COUNT)

    #Part - 4
    # Can threads speed up our CPU-bound tasks ?
    '''Well, it did kick off our threads at the same time initially, but in the end, we see that the whole program execution took about a whopping 40 seconds!
     What just happened? This is because when Thread-1 started, it acquired the Global Interpreter Lock (GIL) which prevented Thread-2 to 
     make use of the CPU. Hence, Thread-2 had to wait for Thread-1 to finish its task and release the lock so that it 
     can acquire the lock and perform its task. This acquisition and release of the lock added overhead to the total execution time. 
     Therefore, we can safely say that threading is not an ideal solution for tasks that requires CPU to work on something.'''

    # t1 = Thread(target = cpu_bound, args = (COUNT, ))
    # t2 = Thread(target = cpu_bound, args = (COUNT, ))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    # Part-5
    # So, splitting the tasks as separate processes work ?
    # p1 = Process(target = cpu_bound, args = (COUNT, ))
    # p2 = Process(target = cpu_bound, args = (COUNT,))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    # Multiprocessing is the answer. Here the MainProcess spins up two subprocesses, having different PIDs, each of
    # which does the job of decreasing the number to zero. Each process runs in parallel, making use of separate CPU
    # core and its own instance of the Python interpreter, therefore the whole program execution took only 8 seconds.
    # Each process executes the function in its own default thread, MainThread. Open your Task Manager during the
    # execution of your program. You can see 3 instances of the Python interpreter, one each for MainProcess,
    # Process-1, and Process-2. You can also see that during the program execution, the Power Usage of the two
    # subprocesses is “Very High”, as the task they are performing is actually taking a toll on their own CPU cores,
    # as shown by the spikes in the CPU Performance graph.

    # Part - 6
    # Multi-processing for our IO bound tasks-
    p1 = Process(target = io_bound, args = (SLEEP, ))
    p2 = Process(target=io_bound, args=(SLEEP,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    '''
    Now that we got a fair idea about multiprocessing helping us achieve parallelism, we shall try to use this 
    technique for running our IO-bound tasks. We do observe that the results are extraordinary, just as in the case of 
    multithreading. Since the processes Process-1 and Process-2 are performing the task of asking their own CPU core 
    to sit idle for a few seconds, we don’t find high Power Usage. But the creation of processes itself is a CPU heavy 
    task and requires more time than the creation of threads. Also, processes require more resources than threads. 
    Hence, it is always better to have multiprocessing as the second option for IO-bound tasks, with multithreading 
    being the first.
    '''

    # Bottomline: Multithreading for IO-bound tasks. Multiprocessing for CPU-bound tasks.

    end = time.time()

    print("Time taken in secs : ", end - start)