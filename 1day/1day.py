name = input('请输入名字')
f = open('name','r')
content = f.read()

position = name.rfind('.')
newname = name[:position]+'back'+name[position:]

f1 = open(newname,'w')
f1.write(content)

f.close()
f1.close()
