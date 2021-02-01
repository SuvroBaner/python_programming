import socket
from _thread import *
import threading

print_lock = threading.Lock()

# Thread function -

def threaded(c):
    while True:
        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')
            # lock released on exit-
            print_lock.release()
            break

        # reverse the given string with client
        data = data[::-1]

        # send back reversed string to the client
        c.send(data)
    # connection closed
    c.close()

def Main():
    host = ""
    # reserve a port on your computer
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print('Socket is listening')

    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client-
        print_lock.acquire()
        print('Connected to: ', addr[0], ':', addr[1])

        # start a new thread and return its identifier
        start_new_thread(threaded, (c, ))
    s.close()

if __name__ == '__main__':
    Main()