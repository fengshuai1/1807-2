import random
class digua():
	def __init__(self):
		self.zhuangtai = '生的'#烤的状态
		self.times = 0#烤的时间
		self.zl = []#装作料

	def __str__(self):
		msg = '我烤的程度是%s'%(self.zhuangtai,str(self.zl))
		return msg

	def cook(self,time):
		self.times+=time
		if self.times >= 1 and self.times <= 2:
			self.zhuangtai = '生的'
		elif self.times >= 3 and self.times <= 5:
			self.zhuangtai = '半生不熟'
		elif self.times >= 6 and self.times <= 8:
			self.zhuanngtai = '8分数'
		elif self.times >= 9 and self.times <= 12:
			self.zhuangtai = '熟了'
		elif self.times > 12:
			self.zhuangtai = '糊了'

	def addzuoliao(self,a):
		self.list.append()

for i in range(15):
    digua.cook()
    if i == 1:
        digua.addZuoLiao("盐")
    elif i == 3:
        digua.addZuoLiao("糖")
    elif i == 5:
        digua.addZuoLiao("麻油")
    digua.tellStatus()
    time.sleep(1)
