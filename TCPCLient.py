import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.1.51', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    # Send data
    message = input()
    print('sending {!r}'.format(message))
    sock.sendall(message.encode('utf-8'))
finally:
    print('closing socket')
    sock.close()