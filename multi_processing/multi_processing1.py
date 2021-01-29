# A multi-processing system can have multiprocessor (a computer with more than 1 CPU)
# A multi-processing system can have multi-core processor (a single computing component with two or more independent
# actual processing units ("cores"))

# Here, the CPU can easily execute several tasks at once with each task using its own processor.

import multiprocessing

def print_cube(num):
    print("Cube: {}".format(num*num*num))

def print_square(num):
    print("Square: {}".format(num*num))

if __name__ == '__main__':
    p1 = multiprocessing.Process(target = print_square, args = (10, ))
    p2 = multiprocessing.Process(target = print_cube, args = (10, ))

    #starting process - 1
    p1.start()
    #starting process - 2
    p2.start()

    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()

    # both processes finished
    print('Done !')