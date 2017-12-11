l=[]
def f():
    for i in range(1,21):
        l.append(i**2)
    print l
    print l[0:5]
    t=tuple(l)
    print t
f()