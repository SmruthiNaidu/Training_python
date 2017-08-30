#constructor chaining
class person:
	nationality='Indian'
	def __init__(self,f,l):
		self.fname=f
		self.lname=l
	def sayhi(self):
		print('hi all!')
class Employee(Person):
	org='Capgemini'
	def __init__ (self,f,l,dept,eid):
		super(). __init__ (f,l)
		self.dept=dept
		self.id=eid
	def work(self)
		print(self.fname+' is busy working)
	def showData(self)
		print ('Name: +self.fname+' '+self.lname+' ID: 'self.id)
class Manager(Employee):
	def __init__(self,f,l,eid,reportees):
		super().__init__(f,l,dept,eid)
e1=Manager('Smruthi','B','Automation','85070',[])
e1.sayhi()
e1.showData()
ptint(type(e1)) 
