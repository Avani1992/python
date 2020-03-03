class Parent:
    def m1(self):
        print("Parent class")

class Child(Parent):
    def m2(self):
        print("Child class")

c=Child()
c.m1()
c.m2()

# o/p:
# Parent class
# Child class