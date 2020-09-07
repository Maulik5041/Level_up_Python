"""Setting up the client server"""


import socket


# Maximum size of a UDP Datagram
MAX_SIZE_BYTES = 65535

# Setting up a socket
s_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f'The OS assigned the address {s_obj.getsockname()} to me')

# Reading the data
message = input('Input lowercase sentence:')
data = message.encode('ascii')

# Sending to the server after encoding to byte stream
s_obj.sendto(data, ('127.0.0.1', 3000))
print(f'The OS assigned the address {s_obj.getsockname()} to me')

# Receiving the server's response
data, address = s_obj.recvfrom(MAX_SIZE_BYTES)

# Decoding and printing the capitalized message
text = data.decode('ascii')
print(f'The server {address} replied with {text}')
