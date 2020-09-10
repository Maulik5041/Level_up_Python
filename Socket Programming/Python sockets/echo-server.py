"""The server will simply echo whatever it receives from the client"""


import socket


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-priviledged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_obj:
    s_obj.bind((HOST, PORT))
    s_obj.listen()
    conn, addr = s_obj.accept()

    with conn:
        print(f'Connected by {addr}')

        while True:
            data = conn.recv(1024)

            if not data:
                break

            conn.sendall(data)
