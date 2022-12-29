class A:
    def __init__(self):
        print("A init exicuted")
        
class b(A):
    def __init__(self):
        print("a init exicuted")
abc=b()
class A:
    def __init__(self):
        print("A init exicuted")
        
class b(A):
    def __init__(self):
        super().__init__()
        print("B init exicuted")
abc=b()

class SchoolName:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('(Initialized SchoolMember{}'.format(self.name))
    def tell(self):
        print('Name:"{}" Age:"{}"'.format(self.name,self.age),end=" ")

class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary
        print('(Initialized Teacher: {})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))
#MRO
class A:
    pass
class B(A):
    pass
class C(B):
    x=5
class D(A):
    x=10
class E(C,D):
    pass
e=E()
print(e.x)
E.mro()
a=range(5)
it=a.__init__()
it.__next__()
class myrange():
    def __init__(self,a):
        self.a=a
    def __iter__(self):
        pass
class myrange_iteration:
    def __init__(self,myrange):
        self.myrange=myrange
        self.i=0
    def next(self):
        ret=self.i
        self.i+=1
        if ret >= self.myrange.n:
            raise StopIteration
        return ret