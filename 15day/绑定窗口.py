from socket import *

s = socket(AF_INET,SOCK_DGRAM)#创建一个udp的套接字

s.bind(('',8888))#绑定端口
#发送
s.sendto("美女约吗".encode("gb2312"),("172.20.10.2",8080))

while True:
	msg = s.recvfrom(1024)

	print("消息是:%s 来自ip:%s"%(msg[0].decode("gb2312"),msg[1][0]))

s.close()
