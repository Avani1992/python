from abc import *
#1. Without ABC and with  abstract method object creation  possible...
class Test:
    @abstractmethod
    def m1(self):
        pass

t=Test()
t.m1()
#2. With ABC and without abstract method object creation  possible...

class Test(ABC):
    def m1(self):
        print("Normal Method...")

t1=Test()
t1.m1() # Normal method..

#3.  With ABC and abstract method object creation not possible...
class Test(ABC):
    @abstractmethod
    def m1(self):
        pass

#t=Test()
#t.m1() # TypeError: Can't instantiate abstract class Test with abstract methods m1

#3. With ABC and abstract method object creation not possible...with child class object possible..

class Test(ABC):
    @abstractmethod
    def m1(self):
        pass

class Child(Test):
    def m1(self):
        print("Abstaract method of Parent class...")

c=Child()
c.m1() # Abstaract method of Parent class...