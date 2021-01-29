# In multiprocessing, any newly created process will do the following -

# 1. Run Independently 2. Have their own memory space

import multiprocessing

# empty list with global scope -
result = []

def square_list(mylist):
    global result
    for num in mylist:
        result.append(num**2)

    print("Result(in process p1): {}".format(result))

if __name__ == '__main__':
    my_list = [1, 2, 3, 4]

    p1 = multiprocessing.Process(target = square_list, args = (my_list, ))
    p1.start()
    p1.join()

    print("Result (in main program): {}".format(result))

#In above example, we try to print contents of global list result at two places:

#In square_list function. Since, this function is called by process p1,
# result list is changed in memory space of process p1 only.
#After the completion of process p1 in main program. Since main program is run by a different process,
# its memory space still contains the empty result list.