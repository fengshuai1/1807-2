class B():
	def __init__(self,name):
		self.name = name
		print('父类的')
	def show(self):
		print('爸爸')

class A(B):
	def __init__(self,name):
		self.name = name
		print('子类')
	def show1(self):
		print('儿子')

a = A('最好')
a.show()
a.show1()



