l=[]
for i in range(0,5):
    string=raw_input()
    a=string.split(',')
    l.append(tuple(a))
    l.sort()
print l
