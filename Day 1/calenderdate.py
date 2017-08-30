#Program to find day of particular date
year=int(input("enter a year:"))
if year%4==0 or year%400==0 and year%100!=0:
	leap_year = True
else:
	leap_year = False

month = int(input("enter a month from [1-12]: "))

if month in (1,3,5,7,8,10,12):
	month_days =31
elif month == 2:
	if leap_year:
		month_days = 29
	else:
		month_days = 28
else:
	month_length = 30


