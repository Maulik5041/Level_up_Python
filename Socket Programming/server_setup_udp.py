"""Setting up a UDP server"""


import socket


# Maximum size of UDP datagram
MAX_SIZE_BYTES = 65535

# Creating socket object - socket.socket(family, type, proto, fileno)
s_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 3000
hostname = '127.0.0.1'

# Binding the socket - socketObject.bind((IP address, port))
s_obj.bind((hostname, port))
print(f'Listening at {s_obj.getsockname()}')

# Making the server listen infinitely with data no larger than 65535 bytes
while True:
    data, client_address = s_obj.recvfrom(MAX_SIZE_BYTES)

    # Decoding the data from byte stream to ASCII
    message = data.decode('ascii')
    upper_case_message = message.upper()

    print(f'The client at {client_address} says {message}')

    # Encoding the message again to bytes
    data = upper_case_message.encode('ascii')

    # Sending the data back to the client
    s_obj.sendto(data, client_address)
