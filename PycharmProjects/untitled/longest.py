s='middle-Outz'
n=11
k=2
l=[]
for i in s:
    result=ord(i)+2
    if (ord(i)<48):
        result=i
    if (ord(i)==122):
        result=ord('a')+1
        result
    l.append(result)
print l
l2=[]
for i in range(len(l)):
    if (l[i]=='-'):
        l2.append('-')
        i=i+1
    else:
        l2.append(chr(l[i]))
print ''.join(l2)




