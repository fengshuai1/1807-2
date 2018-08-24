class student():
	count = 0
	def __init__(self,name):
		self.name = name
		student.count+=1
	def ji(self):
		print('学生')
	@classmethod
	def getcount(cls):
		return cls.count

a = student('赵')
a = student('孙')
a = student('老')

a.ji()
print(a.getcount())

