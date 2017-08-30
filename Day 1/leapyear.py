yr=int(input("enter a year:"))
if yr%4==0 or yr%400==0 and yr%100!=0:
	print ("it is a leap year",yr)
else:
	print ("it is not a leap year",yr)
