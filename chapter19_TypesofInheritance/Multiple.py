# class Parent:
#     def m1(self):
#         print("Parent class")
#
# class Child:
#     def m2(self):
#         print("Child class")
#
# class Child1(Parent,Child):
#     def m3(self):
#         print("Child1 class")
#
# c=Child1()
# c.m1()
# c.m2()
# c.m3()

#2. Both class same method. First come First Serve
#
# class Parent:
#     def m1(self):
#         print("Parent class")
#
# class Child:
#     def m1(self):
#         print("Child class")
#
# class Child1(Parent,Child):
#     def m3(self):
#         print("Child1 class")
#
# c=Child1()
# c.m1()
# c.m1()
# c.m3()

# o/p:
# Parent class
# Parent class
# Child1 class

#3.

#
# class Parent:
#     def m1(self):
#         print("Parent class")
#
# class Child:
#     def m1(self):
#         print("Child class")
#
# class Child1(Child,Parent):
#     def m3(self):
#         print("Child1 class")
#
# c=Child1()
# c.m1()
# c.m1()
# c.m3()
#
# o/p:
# Child class
# Child class
# Child1 class