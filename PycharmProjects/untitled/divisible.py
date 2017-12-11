from __future__ import print_function
start=int(input("start range number:"))
end=int(input("End range number:"))
for i in range (start,end):
    if ((i%3==0) and (i%5!=0)):
        print (i,end=",")