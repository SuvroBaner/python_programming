import socket

def Main():
    # local host IP
    host = '127.0.0.1'

    # define the port on which you want to connect -
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to server on local computer
    s.connect((host, port))

    # message you send to server -
    message = 'This is a test message from the client'
    while True:
        # message sent to server -
        s.send(message.encode('ascii'))

        # message received from the server -
        data = s.recv(1024)

        # print the received message -
        print('Received from the server : ', str(data.decode('ascii')))

        # ask the client whether he wants to continue
        ans = input('\Do you want to continue (y/n) :')
        if ans == 'y':
            continue
        else:
            break

    # close connection
    s.close()

if __name__ == '__main__':
    Main()