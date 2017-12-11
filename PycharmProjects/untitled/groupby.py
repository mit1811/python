from itertools import groupby
things=[("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]
for key,group in groupby(things,lambda x:x[0]):
    print key,list(group)
    #for thing in group:
        #print "A %s is %s" %(thing[1],key)