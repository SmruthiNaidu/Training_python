#Operator Overloading
class Person:
	def __init__(self,f,l):
		self.fname=f
		self.lname=l
	def __str__(self):
		return 'Name:{fname}{lname}'.format(**self.__dict__)
	
li=[
	Person ('Sachin','Tendulkar'),
	Person ('Dhoni','Mahendran'),
	Person ('Sourav','Ganguly'),
	Person ('Yuvraj','Singh'),
	Person ('Anil','Kumbley'),
	]
def my(e):
	return e.fname
#sort in ascending order
li.sort(key=my)
for e in li:
	print(e)
	
#sort in descending order

li.sort(reverse=True,key=my)
for e in li:
	print(e)

	