#MRO
class A:
	def sayhi(self):
		print('A')
class B(A):
	def sayhi(self):
		print('B')
		
class C(B,A):
	def sayhi(self):
		print('C')
		
cl=C()
cl.sayhi()
