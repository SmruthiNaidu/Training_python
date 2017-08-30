#Program to find fibonacci series
p=int(input("enter a number:"))
i=0
j=1
print(i)
print(j)
z=0
count=0
while count < p-2:
	z=i+j
	print(z)
	i=j
	j=z
	count+=1