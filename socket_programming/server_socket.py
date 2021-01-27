# A simple server-client program.

# Server : It uses the bind() which binds it to a specific ip and port so that it can listen to incoming requests
# on that ip and port.  A server has a listen() which puts the server into the listen mode. This allows the server
# to listen to incoming connections.

# https://www.geeksforgeeks.org/socket-programming-python/

import socket

s = socket.socket()
print("Socket created successfully")

# reserve a port on your computer.
port = 12345

# Bind to this port. The ip will be kept empty so that the server listens to requests coming from other computers
# in the network.

s.bind(('', port))
print("Socket binded to %s" %(port))

# If we would have passed 127.0.0.1 then it would have listened to only those calls made within the local computer.

# Put the socket in the listening mode i.e. enable a server to accept connections -
s.listen(5) # backlog = 5
# 5 connections are kept waiting if the server is busy and
# if a 6th socket trys to connect then the connection is refused.
print("Socket is listening")

# a forever loop until we interrupt it or an error occurs
while True:
    # Establish connection with the client
    c, addr = s.accept() # wait for incoming connection.
    # 'c' -> returns a new socket representing a connection and 'addr' -> returns the address of the client
    print('Got connection from ', addr)
    # sending a message back to the client -
    c.send(b"Thanks for connecting")
    # close the connection with the client -
    c.close()


