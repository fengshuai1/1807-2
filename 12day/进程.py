import os
pid = os.fork()
if pid == 0:
	print('111%d'%os.getpid())
else:
	print('222%d'%os.getpid())
