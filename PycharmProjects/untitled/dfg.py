l=[1,2,3,3,3,4,1]
a=set(l)
#print a
b=list(a)
print b
l1=[]
for i in a:
    result=l.count(i)
    l1.append(result)
print l1
d=dict(zip(b,l1))
print d