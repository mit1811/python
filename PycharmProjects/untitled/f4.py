s1=raw_input()
s2=raw_input()
def f(a,b):
    if (len(a) > len(b)):
        print a
    elif (len(a) == len(b)):
        print a
        print b
    else:
        print b
print f(s1,s2)