dict={}
def square(dict):
     for i in range(1,21):
         dict[str(i)]=i**2
     print dict.keys()
square(dict)