def num(a,b):
	def num1(x):
		return a*x+b
	return num1
num1 = num(1,2)
print(num1(3))
