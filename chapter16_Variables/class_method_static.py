class Test:
     a=10
     def __init__(self):
         self.b=20
     @classmethod
     def m1(cls):
         cls.a=888 # Test.a
         cls.b=999 # Test.b

t1=Test()
t2=Test()
t1.m1()
print(t1.a,t1.b)   # 888 20
print(t2.a,t2.b)   # 888 20
print(Test.a,Test.b) # 888 999