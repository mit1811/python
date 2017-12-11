l=[]
for i in range(0,4):
    string=raw_input()
    #_split=string.split(' ')
cmd=string[0]
value=string[1:]
for i in range(0,4):
    if (cmd=='UP'):
       value+=1
    elif (cmd=='DOWN'):
       value-=1
    elif (cmd=="LEFT"):
       value-=1
    elif (cmd=="RIGHT"):
       value+=1
l.append(sum(str(value)))
print l
