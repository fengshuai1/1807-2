import time
import os

num = 0
pid = os.fork()

if pid == 0:
	time.sleep(3)
	print('子进程')
	print('子进程%d'%num)
else:
	print('父进程')
	num+=1
	print('父进程%d'%num)


