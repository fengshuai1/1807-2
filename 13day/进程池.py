from multiprocessing import Pool
import time
def show():
	for i in range(10):
		time.sleep(1)
		print('haah')

p = Pool()
for i in range(3):
	p.apply_async(show)
	#p.apply(show)
	print('1111')


p.close()
p.join()
print('3333')







