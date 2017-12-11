def evallist(l):
    a = set(l)
    # print a
    b = list(a)
    #print b
    l1 = []
    for i in a:
        result = l.count(i)
        l1.append(result)
    #print l1
    d = dict(zip(b, l1))
    print d
evallist([1,2,3,4,5,5,5,6,3,2])