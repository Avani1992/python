class Parent:
    def m1(self):
        print("Parent class")

class Child(Parent):
    def m2(self):
        print("Child class")

class Child1(Child):
    def m3(self):
        print("Child1 class")

class Child2(Child1):
    def m4(self):
        print("Child2 class")

c=Child2()
c.m1()
c.m2()
c.m3()
c.m4()