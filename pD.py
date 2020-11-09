import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 13001)
print(f'starting up on {server_address[0]} port {server_address[1]}')
sock.bind(server_address)
sock.listen(1)

first_interval = 0
second_interval = 0

def listening():
    while True:
        global first_interval
        global second_interval
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('client connected:', client_address)
            while True:
                data = connection.recv(16)
                data = data.decode("utf-8")
                """need to split data into two variables: pitch and envelope"""
                data = data.replace('\n', '').replace('\t','').replace('\r','').replace(';','')
                if not data:
                    break
        finally:
            connection.close()


listening()