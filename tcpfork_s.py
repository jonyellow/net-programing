from socket import *
from os import fork

def child(c):
    while 1:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        data = input('you:')
        c.send(data.encode())
    c.close()

def father():
    sockfd = socket(AF_INET, SOCK_STREAM)
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(('127.0.0.1', 8000))
    sockfd.listen(5)
    while 1:
        print('waitting for connect')
        c, addr = sockfd.accept()
        print('coonecting with', addr)

        pid = fork()
        if pid == 0:
            sockfd.close()
            child(c)
        else:
            c.close()
            continue

if __name__ == "__main__":
    father()