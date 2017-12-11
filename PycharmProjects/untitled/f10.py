t=(1,2,3,4,5,6,7,8,9,10)
l1=[]
def f():
    for i in t:
        if (i%2==0):
            l1.append(i)
    t1=tuple(l1)
    print t1
f()