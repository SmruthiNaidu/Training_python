#prime with for in range
isPrime='Prime'
d=int(input('Enter a number'))
for i in range(2,d):
	if d%i==0:
		print('Not a Prime')
		break
else:
	print('isPrime')
	
