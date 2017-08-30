def fact(n):
	if n>0:
		value=n*fact(n-1)
		return value
	else:
		return 1
print(fact(5))
