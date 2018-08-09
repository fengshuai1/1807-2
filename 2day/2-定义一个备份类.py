class lei():
	def name(self):
		name = input("请输入备份文件名字（要有后缀名）")
		f = open(name,"r")

		position = name.rfind(".")
		newname = name[:position]+"备份"+name[position:]
		f1 = open(newname,"w")
		while True:
			content = f.read(1024)
			f1.write(content)
			if len(content) == 0:
				break

		f.close()
		f1.close()
a = lei()
a.name()
