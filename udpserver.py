import traceback
from socket import *
import sys

#创建udp套接字server

#绑定IP地址，端口
from time import sleep

if len(sys.argv) == 3:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
else:
    print('argvError')
    sys.exit('服务器退出')



#创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)
#绑定地址、、端口
sockfd.bind((HOST,PORT))
#阻塞接听消息：
while 1:
    try:
        data, addr = sockfd.recvfrom(1024)
        print("continue at{}".format(addr))
    except KeyboardInterrupt:
        sockfd.close()
        sys.exit('服务器退出！')
    except Exception:
        traceback.print_exc()
    sleep(0.2)
    print(data.decode())
    sockfd.sendto(b'massage arrived!', addr)