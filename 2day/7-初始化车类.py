class car():
	def __init__(self,yanse,xinghao):#魔法方法 实例方法
		self.yanse = yanse
		self.xinghao = xinghao

	def __str__(self):#魔法方法
		msg = '车的颜色%s,车的型号%s'%(self.yanse,self.xinghao)
		return msg
	def run(self):
		print('跑')
	def ting(self):
		print('听音乐')
	

baoma = car('黑色','宝马')#创建一个车对象
baoma.run()
baoma.ting()
print(baoma)
