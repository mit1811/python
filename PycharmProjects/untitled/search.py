import re
item=[x for x in raw_input().split()]
value=[]
for i in item:
    if len(i)<6 or len(i)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",i):
        continue
    elif not re.search("[A-Z]",i):
        continue
    elif not re.search("[0-9]",i):
        continue
    elif not re.search("[$#@]",i):
        continue
    elif not re.search("\s",i):
        continue
    else:
        pass
    value.append(i)
print ''.join(value)