#construction chaining with multi level inheritance
class Person:
	Nationality='Indian'
	def __init__(self,f,l):
		self.fname=f
		self.lname=l
	def sayhi(self):
		print ('Hi All')

class Employee(Person):
	org='Capgemini'
	def __init__(self,f,l,d,e):
		super().__init__(f,l)
		self.dept=d
		self.id=e
		
	def work(self):
		print(self.fname+'is busy working')
	def showData(self):
		print('Name:'+self.fname+' '+self.lname+' ID: '+self.id)
class Manager(Employee):
	def __init__(self,f,l,dept,eid,reportees):
		super().__init__(f,l,dept,eid)
		self.reportees=reportees
	def test(self):
		print(hasattr(self,'dept'))
		print(getattr(self,'dept'))
		
e1=Manager('Smruthi','B','Automation','85070',[])
e1.sayhi()
e1.showData()
print(type(e1))

e1.test()


	