s=raw_input()
d={"letters":0,"digits":0}
for i in s:
    if i.isalpha():
        d["letters"]+=1
    elif i.isdigit():
        d["digits"]+=1
print "letters",d["letters"]
print "digits",d["digits"]

