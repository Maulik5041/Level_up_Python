"""Connecting the server and client code"""


import argparse
import socket


# Maximum size of a UDP Datagram
MAX_SIZE_BYTES = 65535

def server(port):

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


def client(port):
    host = '127.0.0.1'

    # Setting up a socket
    s_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # For the added security of only using a specific address
    s_obj.connect((host, port))
    print(f'The OS assigned the address {s_obj.getsockname()} to me')

    # Reading the data
    message = input('Input lowercase sentence:')
    data = message.encode('ascii')

    # Sending to the server after encoding to byte stream
    # s_obj.sendto(data, ('127.0.0.1', 3000))
    s_obj.send(data)
    print(f'The OS assigned the address {s_obj.getsockname()} to me')

    # Receiving the server's response
    #data, address = s_obj.recvfrom(MAX_SIZE_BYTES)
    data = s_obj.recv(MAX_SIZE_BYTES)

    # Decoding and printing the capitalized message
    text = data.decode('ascii')
    print(f'The server replied with {text}')


if __name__ == '__main__':
    funcs = {"client": client, "server": server}
    parser = argparse.ArgumentParser(description='UDP client and server')
    parser.add_argument('functions', choices=funcs, help='client or server')
    parser.add_argument('-p', metavar='PORT', type=int, default=3000,
                        help='UDP port (default 3000)')
    args = parser.parse_args()
    function = funcs[args.functions]
    function(args.p)
