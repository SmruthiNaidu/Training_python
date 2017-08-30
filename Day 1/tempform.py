temp='Hello {0}{1} , Welcome to {2}'
li=['Mr.','Sachin','Bangalore']
data = temp.format(*li)
print(data)


temp= '''Hello {title} {name} , Welcome to {city}
	how was your journey'''
data=temp.format(title='Mr.',name='Sachin',city='Bangalore')
print(data)

temp= 'Hello {title} {name} , Welcome to {city}'
d={'title':'Mr.','name':'Sachin','city':'Bangalore'}
data=temp.format(**d)
print(data)
