#filter out cool cities
class city:
	def __init__(self,c,temp,des):
		self.country=c
		self.temperature=temp
		self.description=des
	def __str__(self):
		return 'city:{country}{temperature}{description}'.format(**self.__dict__)
	def __lt__(s,o):
		return s.temperature < o.temperature
		

a=city('India','30','cool')
b=city('Pakistan','50','hot')
c=city('Canada','20','cool')
li=[a,b,c]

def my(e):
	return e.temperature
li.sort(key=my)
for e in li:
	print(e)


	
