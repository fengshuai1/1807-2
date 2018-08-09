class cai():
	def shu(self):
		import random
		i = 0
		a = random.randint(1,50)#电脑
		while True:
			b = int(input("请输入数字"))
			if b > a:
				print("数大了")
			elif b < a:
				print("数小了")
			else:
				print("猜对了")
				break
#			i = 10
#			i+=1

a = cai()
a.shu()
