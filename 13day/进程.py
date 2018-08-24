from multiprocessing import Process
import time

def show(name):
	for i in range(10):
		time.sleep(2)
		print(name)
p = Process(target=show,args=('割草',))
p.start()#启动进程

p.join() #等待子进程结束，再往下运行
p.join(3) #最多三秒

#time.sleep(3)
#p.terminate()#不管子进程结束没结束，立马让子进程停止
print('吃喝玩乐')


