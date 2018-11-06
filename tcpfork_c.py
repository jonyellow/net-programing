from socket import *

sockfd = socket(AF_INET, SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(('127.0.0.1', 8881))

sockfd.connect(('127.0.0.1', 8000))

while 1:
    data = input('you:')
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    if not data:
        break
    print(data.decode())
sockfd.close()