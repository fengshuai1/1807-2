class home():
	def __init__(self,name,area):
		self.name = name
		self.area = area
		self.list = []
	def __str__(self):
		msg = '我的家在%s 大小是%d'%(self.name,self.area)
		return msg
	def zhuangjiaju(self,jiaju):
		if self.area < self.area:
			print('空间不足')
		else:
			self.list.append(jiaju)
			self.area = self.area - jiaju.area
		
class bad():
	def __init__(self,name,area):
		self.name = name
		self.area = area
	def __str__(self):
		msg = '床的名字%s 大小%d'%(self.name,self.area)
		return msg
a = home('北京',100)
print(a)
b = bad('好梦',5)
print(b)
for i in range(50):
	if a.area < b.area:
		print('装不下')
		break
	else:
		a.zhuangjiaju(b)
