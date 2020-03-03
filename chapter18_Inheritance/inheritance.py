class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eatndrink(self):
        print('Eat Biryani and Drink Beer')

class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age) # Calling parent class constructor...
        self.eno=eno
        self.esal=esal

    def work(self):
        print("Coding Python is very easy just like drinking Chilled Beer")
    def empinfo(self):
        print("Employee Name:",self.name)
        print("Employee Age:",self.age)
        print("Employee Number:",self.eno)
        print("Employee Salary:",self.esal)

e=Employee(' Prasanna', 48, 100, 10000)
e.eatndrink()
e.work()
e.empinfo()
