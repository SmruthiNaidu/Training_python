year=int(input('Enter the year'))
month=int(input('Enter the month'))
date= int(input('Enter the date'))

if month<=0 and month>=12:
	 print('Invalid month')
else:
	i=0
	doy=0
	lom=[31,28,31,30,31,30,31,31,30,31,30,31]
	while i+1<month:
		doy=doy+lom[i]
		i+=1
	date=date+doy
	
	if date%7==1:
		print('sunday')
	elif date%7==2:
		print('Monday')
	elif date%7==3:
		print('Tuesday')
	elif date%7==4:
		print('Wednesday')
	elif date%7==5:
		print('Thrusday')
	elif date%7==6:
		print('friday')
		
	else:
		print('saturday')

	
			                                                                                                                                                                                                                                                                                                                   

