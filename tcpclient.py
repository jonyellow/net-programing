from socket import *

#创建套接字
sockfd = socket(AF_INET, SOCK_STREAM)
#设置端口重用
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
#绑定客户端地址
sockfd.bind(('127.0.0.1', 5050))

#连接服务器
sockfd.connect(('127.0.0.1', 5005))

while 1:
    data = input('you:')
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    if not data:
        break
    print(data.decode())
sockfd.close()