d1 = {'a': 100, 'b': 700, 'c':500}
d2 = {'a': 300, 'b': 200, 'd':600}
d={}
for key1,value1 in d1.items():
    for key2,value2 in d2.items():
        if key1 == key2:
            d[key1]=d1[key1]+d2[key2]
        if key1 not in d:
            d[key1]=d1[key1]
        if key2 not in d:
            d[key2]=d2[key2]
print d


