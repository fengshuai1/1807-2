class cai():
	def quan(self):
		i = 0
		while i < 5:
			import random
			computer = random.randint(1,3)#电脑玩家
			player = int(input("请输入1:石头 2:剪子 3:布"))
			if player <= 3 and player > 0:
				if (player ==1 and computer == 2) or (player == 2 and computer == 3) or(player == 3 and computer ==1):
					print("你赢了")
				elif player == computer:
					print("平局")
				else:
					print("你输了")
			else:
				print("输入不合法")
			i+=1 #i = i+1

a = cai()
a.quan()
