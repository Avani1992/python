class P:
    a=10
    def __init__(self):
        self.b=20

class C(P):
    def m1(self):
        print(super().a)#valid 10
        print(self.b)#valid 20
        print(super().b)#invalid Attribute Error..
c=C()
c.m1()