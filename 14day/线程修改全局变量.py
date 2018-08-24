from threading import Thread
import time
num = 0
def work1():
	global num
	m.acquire(True)#加锁
	for i in range(10000000):
		
		num+=1
	m.release()#释放锁
	print('111')
	print(num)
def work2():
	global num
	m.acquire(True)
	for i in range(10000000):
		num+=1
	m.release()
	print('222')
	print(num)
	break
a = Thread(target=work1)
a1 = Thread(target=work2)
a.start()
a1.start()
