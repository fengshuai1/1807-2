#list = [{'name':'老王'},{'age':'老宋'}]
'''
f = open('11,22','w')
f.write(str(list))
f.close()
'''



list = []


f1 = open('11,22','r')
a = f1.read()
print(type(a))
list = eval(a)
for i in list:
	for k,v in i.items():
		print(k,v)
print(list)
f1.close()
