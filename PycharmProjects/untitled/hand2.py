import os
import sys
p='C:/Users/Mit/PycharmProjects/untitled/wx_data/'
file1=open('C:/Users/Mit/Documents/python/assignmentfilehandling/answers/missingdata.txt','w')
file2=open('C:/Users/Mit/Documents/python/assignmentfilehandling/answers/maxmin.txt','w')
dirs=os.listdir(p)
count1=0
for f in dirs:
    print f
    filename=f
    f=open(p+filename,'r')
    count2=0
    for line in f:
        s=line
        s=s.split()
        val='-9999'
        if (s[3]==val):
            if(s[1]!=val and s[2]!=val):
                count1+=1
                count2+=1
    file1.write("{}\t\t{}\n".format(filename,count2))
    print ("file name is {} and missing count is {} ".format(filename,count2))
dirs = os.listdir(p)
count1=0
for f in os.listdir(p):
    print f
    filename=f
    f=open(p+filename,'r')
    count2=0
    _max=0
    _min=0
    _prec=0
    for line in f:
        s=line
        s=s.split()
        val='-9999'
        if (s[1]!=val):
            _max+=int(s[1])
        if (s[2]!=val):
            _min+=int(s[2])
        if (s[3]!=val):
            _prec+=int(s[3])
            count1+=1
    avgmax=_max/count1
    print avgmax
    avgmin=_min/count1
    print avgmin
    avgprec=_prec/count1
    print avgprec
    file2.write("{}\t\t{}\t{}\t{}\n".format(filename,avgmax,avgmin,avgprec))

