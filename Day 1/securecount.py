def outer():
	count=0
	def inner():
		nonlocal count
		count+=1
		print(count)
	return inner
a=outer()
a()
a()
a()
hi=outer()
hi()
hi()