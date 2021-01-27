''' Socket Programming :
A connection between two nodes on a network to communicate with each other. e.g. between a server and a client '''

# Import modules -

import socket
import sys

try:
    # Create a simple socket (address_family ipv4, socket type using TCP protocol, protocol number)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created successfully")
except socket.error as err:
    print("Socket creation failed with the error %s" %(err))

# default port for socket is 80, but it can be anything
port = 80

# Let's connect to a server using this socket. Here we will connect to Google -

try:
    host_ip = socket.gethostbyname('www.google.com')
    print(host_ip)
except socket.gaierror:
    print("There was an error resolving the host")
    sys.exit()

s.connect((host_ip, port))
print("The socket has successfully connected to Google")

# Now, we need to know how can we send data through a socket.
# sendall() allows you to send data to a server to which the socket is connected and server can also send data to the
# client using this function.







