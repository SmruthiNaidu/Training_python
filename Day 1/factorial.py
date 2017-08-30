# Program to find factorialof a given number
num=int(input("enter a number"))
f=1
while num>0:
	f=f*num
	num=num-1
print ("factorial of given number is ",f)