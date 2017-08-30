#Mapping,lambda and Filtering

li=[22,23,21,44,45]
def my(e1):
	return  e1*9/5+32
m=list(map(my,li))
print(m)

#lambda

m=list(map(lambda e1:e1*9/5+32,li))
print(m)

#Filtering

def my(e1):
	return e1<30
	
m=list(filter(my,li))
print(m)