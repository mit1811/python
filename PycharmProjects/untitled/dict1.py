dict={}
item=raw_input()
for word in item.split():
    dict[word]=dict.get(word,0)+1
#print dict.keys()
#print dict.values()
words=dict.keys()
words.sort()
#print words
for i in words:
    print "%s:%d" %(i,dict[i])


