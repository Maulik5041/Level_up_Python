import socket


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_obj:
    s_obj.connect((HOST, PORT))
    s_obj.sendall(b'Hello World')
    data = s_obj.recv(1024)


print(f'Received {repr(data)}')
