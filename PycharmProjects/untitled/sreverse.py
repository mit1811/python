s="H1e2l3l4o5w6o7r8l9d"
l=[]
for i in range(len(s)):
    if (i%2==0):
        l.append(s[i])
print ''.join(l)