a=filter(lambda x:x%2 == 0,[1,2,3,4,5,6,7,8,9,10])
print a
b=map(lambda x:x**2,[1,2,3,4,5,6,7,8,9,10])
print b
c=map(lambda x:x**2,filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8,9,10]))
print c
d=filter(lambda x:x%2==0,range(1,21))
print d
e=map(lambda x:x**2,range(1,21))
print e