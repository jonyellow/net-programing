from socket import *
from time import sleep, ctime
#创建套接字
sockfd = socket(AF_INET, SOCK_STREAM)
#设置端口重用
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
#绑定服务器地址、端口
sockfd.bind(('127.0.0.1', 5005))
#设置监听
sockfd.listen(5)

#等待连接
conn, addr = sockfd.accept()
print('connecting with',addr)
while 1:
    data = conn.recv(1024)
    if not data:
        break
    print(data.decode())
    sleep(0.2)
    data = input('you:')
    conn.send(data.encode())
conn.close()
sockfd.close()