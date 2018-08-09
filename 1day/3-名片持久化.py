list = []#名片容器
while True:
	def num():
		a = {}

		name = input('请输入名字')
		age = int(input('请输入年龄'))
		a['name'] = name
		a['age'] = age
		list.append(a)
		print('添加成功')
#		break
#		q()

	def q():
		w = open('1.txt','w')
		w.write(str(list))
		w.close()
		s()

	def s():
		f1 = open('2.txt','r')
		content = f1.read()
		if len(content) != 0:
			print(type(content))
			list = eval(content)
			for i in list:
				for k,v in i.items():
					print(k,v)
		print(list)
		f1.close()
		num()
