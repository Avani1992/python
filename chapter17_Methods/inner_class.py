# class Outer:
#      def __init__(self):
#          print("outer class object creation")
#
#      class Inner:
#
#          def __init__(self):
#              print("inner class object creation")
#          def m1(self):
#              print("inner class method")
#
# o=Outer()
# i=o.Inner()
# i.m1()
#
# # i= Outer().Inner().m1()

class Person:
     def __init__(self):
         self.name='prasanna'
         self.Dob()

     def display(self):
         print('Name:',self.name)

     class Dob:
         def __init__(self):
             self.dd=10
             self.mm=5
             self.yy=1947

         def display(self):
             print('Dob={}/{}/{}'.format(self.dd,self.mm,self.yy))

p=Person()
p.display()

p.Dob().display()