dic1={'color':'pink','flower':'rose'}
i=iter(dic1)
print(type(i))
while True:
	a=i.__next__()
	print(a)
