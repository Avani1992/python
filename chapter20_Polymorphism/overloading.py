# class A:
#     def m1(self,name):
#         self.n=name
#         print(self.n)
#     def m1(self,name,age):
#         self.n=name
#         self.a=age
#         print(self.n)
#         print(self.a)
# a1=A()
# a1.m1("Avani") # TypeError: m1() missing 1 required positional argument: 'age'
# a1.m1("Kuman",28)


 # Using Variable length we r achiving Method overloading..
class Test:
     def sum(self,*a):
         total=0
         for x in a:
             total=total+x
         print('The Sum:',total)

t1=Test()
t1.sum(10,20)
t1.sum(20,40,60,80)