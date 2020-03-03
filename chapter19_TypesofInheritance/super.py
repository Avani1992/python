class P:
    a=10
    def __init__(self):
        self.b=10
        print("Parent constructor")
    def m1(self):
        print('Parent instance method')
    @classmethod
    def m2(cls):
        print('Parent class method')
    @staticmethod
    def m3():
        print('Parent static method')

class C(P):
    a=888
    def __init__(self):
        self.b=999
        print(self.b)
        super().__init__() # Parent class Constructor

        print(super().a) # Static variable
        super().m1() # instance method
        super().m2() # Class metho
        super().m3() # Static method


    def m1(self):
         print()
         print("Child class Instance method.....")

         super().__init__()
         super().m1()
         super().m2()
         super().m3()

    @classmethod
    def m2(cls):
         print()
         print("Child class Class  method.....")

         super(C,cls).__init__(cls) # can't call parent constructor directly by child class method..use classname,cls bcz constructor and instance method call by object reference variable.
         super(C,cls).m1(cls) #  can't call parent instance method  directly by child class method..use classname,cls
         super().m2()
         super().m3()

    @staticmethod
    def m3():
        print()
        print("Child class Static  method.....")

        # super().__init__()  # can't call parent constructor  by child static method..
        # super().m1()  # can't call parent instance method   by child Static method..
        # super().m2()
        super(C,C).m3() # only parent class static method call in child class static method using child class name..


# c=C()
# c.m1() # for constructor and instance method
C.m2() # class method
C.m3() # static method..

# o/p:
# 999
# 10
# Parent instance method
# Parent class method
# Parent static method

#2.
#
# class A:
#     def m1(self):
#         print('A class Method')
# class B(A):
#     def m1(self):
#         print('B class Method')
# class C(B):
#     def m1(self):
#         print('C class Method')
# class D(C):
#     def m1(self):
#         print('D class Method')
# class E(D):
#     def m1(self):
#         A.m1(self) # A class m1()
#         super(C,self).m1() # B class m1() call parent class method. here B is parent class of C
#
# e=E()
# e.m1()

# o/p:
# A class Method
# B class Method