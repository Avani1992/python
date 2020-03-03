# class Test:
#      a=777
#      @classmethod
#      def m1(cls):
#          cls.a=888
#      @staticmethod
#      def m2():
#          Test.a=999
# print(Test.a)   # 777
# Test.m1()
# print(Test.a)   # 888
# Test.m2()
# print(Test.a)   # 999
#

# 2.

class Test:
     a=10
     def __init__(self):
         self.b=20
t1=Test()
t2=Test()
Test.a=888
t1.b=999
print(t1.a,t1.b)    # 888 999
print(t2.a,t2.b)    # 888 20