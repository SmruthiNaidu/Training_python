#classes
class A:
	def sayhi(self):
		print('A')
class B(A):
	'''this document is to test instances
	'''
	def sayhi(self):
		print('B')
		
class C(B,A):
	def demo(self):
		print(C.__doc__)
		print(C.__bases__)
		print(C.__name__)
		print(C.__dict__) 
		
cl=C()
cl.demo()
