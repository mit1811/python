s=raw_input()
d={"UPER CASE":0,"LOWER CASE":0}
for i in s:
    if (i.isupper()):
        d["UPER CASE"]+=1
    elif (i.islower()):
        d["LOWER CASE"]+=1
print "UPER CASE",d["UPER CASE"]
print "LOWER CASE",d["LOWER CASE"]

