from multiprocessing import Pool
import time

def download():
	for i in range(5):
		time.sleep(1)
	return '完成'

def noti(arg):
	print(arg)
p = Pool()
p.apply_async(download,callback=noti)	
p.close()
for i in range(50):
	print('玩')
	time.sleep(1)



