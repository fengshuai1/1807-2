from socket import *

s = socket(AF_INET,SOCK_DGRAM)#创建一个udp的套接字

s.sendto("帅哥".encode("gb2312"),("172.20.10.2",8080))

s.close()
