num=input("enter input")
def name():
    for i in range(num):
        l=[]
        s1=raw_input("enter name")
        for i in s1:
            l.append(i)
            if (i == '@'):
                l.remove(i)
            a = ''.join(l)
            l1=[]
            l1.append(a)
        print (l1)
print name()