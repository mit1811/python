s=raw_input()
s=s.split()
l=[]
for i in range(len(s)):
    for j in s[i]:
        l.append(j)
print ''.join(l)
a=sorted(set(l))
for i in (a):
    print i,l.count(i)