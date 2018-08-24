def w(type):
	def w1(fun):
		def inner():
			if type == 1:
				print('haha')
			elif type == 2:
				print('111')
			fun()
		return inner
	return w1

@w(1)
def show():
	print('222')

@w(2)
def show1():
	print('333')

a = show()
b = show1()
