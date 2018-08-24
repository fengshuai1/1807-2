def fib():
	a,b = 0,1
#	print('haha')
	for i in range(10):
#		print('111')
		#print(b)
		yield b
#		print('333')
		a,b = b,a+b


#print(fib())
G = fib()
#print(next(G))
for i in G:
	print(i)





