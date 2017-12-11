import sys
amount=0
while True:
    s=raw_input()
    if not s:
        break
    values=s.split(' ')
    operation=values[0]
    netamount=int(values[1])
    if operation=='D':
        amount+=netamount
    elif operation=='W':
        amount-=netamount
    else:
        pass
print amount

