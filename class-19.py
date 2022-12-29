class a:
    name="Ranit"
    marks=90
type(a)
a=6
type(a)
type(object)

class A:
    def __call__(self):
        print("You called me")
 
b=A.__call__()
b=A()
a={"name": "Ranit"}
a["name"]
a.__getitem__("name")

class Exponent:
    def __init__(self,a):
        self.a=a
    def __getitem__(self,x):
        return x**self.a
e=Exponent(3)
e[6]
class dog:
    kind="canine"
    def __init__(self,name):
        self.name=name
a=dog("Tommy")
a.name
class dog:
    tricks=[]
    def __init__(self,name):
        self.name=name
    def add_trick(self,trick):
        self.tricks.append(trick)
di=dog("tom")
di.add_trick("roll")
di.add_trick("jump")
di.tricks
d3=dog("jhonny")
d3.tricks