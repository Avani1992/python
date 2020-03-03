class Book:
     def __init__(self,pages):
         self.pages=pages

     def __add__(self,other):  # Magic method
        return self.pages+other.pages # here self.pages=b1 and othr.pages=b2

b1=Book(100)
b2=Book(200)
print(b1+b2) # error . without __add__
print('The Total Number of Pages:',b1+b2) # 300

#2.

class Book:
    def __init__(self, pages,name):
        self.pages = pages
        self.name=name

    def __add__(self, other):  # Magic method
        return (self.name + other.name,self.pages+other.pages)  # here self.pages=b1 and othr.pages=b2


b1 = Book(100,"Java")
b2 = Book(200,"Python")
print(b1 + b2)  # error . without __add__
print('The Total Number of Pages:', b1 + b2)  # ('JavaPython',300)

#3.

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self,other): # Magic method
        return self.marks>other.marks
    def __le__(self,other): # Magic method
        return self.marks<=other.marks


print("10>20 =",10>20) # False
s1=Student("Prasanna",100)
s2=Student("Ravi",200)
print("s1>s2=",s1>s2) # False
print("s1<s2=",s1<s2) # True
print("s1<=s2=",s1<=s2) # True
print("s1>=s2=",s1>=s2) # False

#4.

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __mul__(self,other):
        return self.salary*other.days

class TimeSheet:
    def __init__(self,name,days):
        self.name=name
        self.days=days

e=Employee('Prasanna',500)
t=TimeSheet('Prasanna',25)
print('This Month Salary:',e*t) # 12500