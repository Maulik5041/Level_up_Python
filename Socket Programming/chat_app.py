"""UDP chat App"""


import argparse
import socket


# Maximum size of a UDP datgram
MAX_SIZE_BYTES = 65535


def server(port):
    s_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = '127.0.0.1'
    s_obj.bind((hostname, port))
    print(f'Listening at {s_obj.getsockname()}')

    while True:
        data, client_address = s_obj.recvfrom(MAX_SIZE_BYTES)
        message = data.decode('ascii')
        print(f'The client at {client_address} says {message}')
        msg_to_send = input('Input message to send to client: ')
        data = msg_to_send.encode('ascii')
        s_obj.sendto(data, client_address)


def client(port):
    s_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = '127.0.0.1'

    while True:
        s_obj.connect((host, port))
        message = input('Input message to send to server: ')
        data = message.encode('ascii')
        s_obj.send(data)
        data = s_obj.recv(MAX_SIZE_BYTES)
        text = data.decode('ascii')
        print(f'The server replied with {text}')


if __name__ == '__main__':
    funcs = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='UDP client and server')
    parser.add_argument('functions', choices=funcs, help='client or server')
    parser.add_argument('-p', metavar='PORT', type=int, default=3000,
                        help='UDP port (default 3000)')
    args = parser.parse_args()
    function = funcs[args.functions]
    function(args.p)
