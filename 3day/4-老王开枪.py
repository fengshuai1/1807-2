class ren():
	def __init__(self,name):
		self.name = name

	def zhuangzidan(self,dj,zd):
		dj.addzidan(zd)
	def zhuangdanjia(self,dj,q):
		q.adddanjia(dj)
	def naqiqiang(self,q):
		self.q = q
	def kaiqiang(self,diren):
		
		self.q.kaihuo(diren)
	def diaoxue(self,count):
		self.hp -= count
		if self.hp <=0:
			print('挂了')
		else:
			print('还剩%d'%(self.sh))




class qiang():
	def __init__(self,name):
		self.name = name
		self.dj = None
	def adddanjia(self,dj):
		self.dj = dj
	def kaihuo(self):
		zidan = self.dj.tandanjia()
		zidan.sharen(diren)





class danjia():
	def __init__(self,count):
		self.count = count
		self.zds = []
	def addzidan(self,zd):
		self.zds.append(zd)
	def tanzidan(self):
		self.zds.pop(0)
		
		



class zidan():
	def __init__(self,name,sh):
		self.name = name
		self.sh = sh
	def sharen(self,diren):
		diren.diaoxue(self.sh)

laowang = ren('老王')
ak47 = qiang('AK47')
dj = danjia(40)
for i in range(40):
	zd = zidan('5.56',5)
	laowang.zhuangzidan(dj,zd)
laowang.zhuangzidan(dj,ak47)
laowang.naqiqiang(ak47)
laosong = ren('老宋')
laowang.kaiqiang(laosong)
