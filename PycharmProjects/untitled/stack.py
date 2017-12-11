class Person():
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name
    def isemp(self):
        return False
class Employee(Person):
    def isemp(self):
        return True
emp=Person("myname")
print emp.getname(), emp.isemp()
emp=Employee("your name")
print emp.getname(), emp.isemp()

class Base():
    pass
class Derived(Base):
    pass
print (issubclass(Derived,Base))
print (issubclass(Base,Derived))
d=Derived()
b=Base()
print (isinstance(d,Base))
print (isinstance(b,Derived))

class Base1():
    def __init__(self,x):
        self.x=x
class Derived1(Base1):
    def __init__(self,x,y):
        Base1.x=x
        self.y=y
    def printxy(self):
        print (Base1.x,self.y)
ob=Derived1(10,15)
print ob.printxy()

class Item1(object):
    def __init__(self,x):
        self.x=x
class Item2(Item1):
    def __init__(self,x,y):
        super(Item2,self).__init__(x)
        self.y=y
    def all(self):
        print (self.x,self.y)
a=Item2(50,100)
print a.all()




