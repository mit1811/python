class Polinomial():
    def __init__(self,*coffe):
        self.coffe=coffe
    def __repr__(self):
        return "polinomial {}".format(self.coffe)
    def __add__(self, other):
        return Polinomial(*(x+y for x,y in zip(self.coffe,other.coffe)))
    def __mul__(self, other):
        return Polinomial(*(x*y for x,y in zip(self.coffe,other.coffe)))
p1=Polinomial(1,2,3)
p2=Polinomial(4,5,6)
print p1
print p2
print p1+p2
print p1*p2



