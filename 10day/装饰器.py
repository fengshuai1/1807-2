def w1(fun):
	def num():
		print('haha')
		fun()
	return num

@w1		#相当于pay = w1(pay)  语法糖
def pay():
	print('111')

pay()

