#from __future__ import print_function
string="hello how are you."
a=string.split()
b=a[-1].split()
print b
a.sort(key=len,reverse=False)


result=' '.join(a)
print result.capitalize()