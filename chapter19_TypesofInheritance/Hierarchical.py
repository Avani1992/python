class Parent:
    def m1(self):
        print("Parent class")

class Child(Parent):
    def m2(self):
        print("Child class")

class Child1(Parent):
    def m3(self):
        print("Child1 class")

c=Child() # child class
c.m1()
c.m2()
print("----------------")
c1=Child1() # child1 class
c1.m1()
c1.m3()