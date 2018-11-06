'''
author: jon
server:127.0.0.1:5000
'''
from time import sleep
from socket import *

#创建套接字udp

sockfd = socket(AF_INET, SOCK_DGRAM)
#向服务器发送请求
while 1:
    data = input('you:')
    sockfd.sendto(data.encode(),('127.0.0.1',5000))
    data, addr = sockfd.recvfrom(1024)
    print('server:',data.decode())