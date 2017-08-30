'''l2=[[x,10-x] for x in range(10)]
print(l2)

print('to avoid repetitions')

l3=[[x,y] for x in range(10) for y in range(x,10) if x+y==10]

print(l3)

print('3 input addition')

l4=[[x,y,z] for x in range(10) for y in range(x,10) for z in range(y,10) if x+y+z==10]

print(l4)

print('list comprehension for factors')

n=int(input('enter a number'))
L=[i for i in range(1,n+1) if n%i==0]
print(L)

print('list of list of factors using list comprehension')
'''
L1=[[i for i in range(1,n+1) if n%i==0] for n in range(1,11)]
print(L1)
