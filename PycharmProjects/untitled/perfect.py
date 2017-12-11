
def name():

    for j in range(1,5000):
        _sum = 0
        for i in range(1,j):
            if (j % i == 0):
                _sum+=i
                if(_sum==j):
                    print ("perfect number is",j)
name()
