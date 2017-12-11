sub=['I','You']
verb=['Play','Love']
ob=['hockey','football']
for i in range(len(sub)):
    for j in range(len(verb)):
        for k in range(len(ob)):
            result="%s %s %s" % (sub[i],verb[i],ob[i])
    print result