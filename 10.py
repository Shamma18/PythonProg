class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        print(self.a+self.b)
ob=MyClass(12,10)
ob.sum()

class Parent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        print(self.a+self.b)
class Child(Parent):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum1(self):
        print(self.a+self.b)
    
m=Parent(12,128)
n=Child(10,109)
n.sum()
n.sum1()
m.sum()
        