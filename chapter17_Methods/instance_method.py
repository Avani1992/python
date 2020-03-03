class Demo:
    def __init__(self):
        print("Constructor....")
    def m1(self):
        a=10 # local variable
        Demo.b=20 # static variable
        self.c=30 # instance variable
        print(a) # 10
    def display(self):
        print(Demo.b) # 20
        print(self.c) # 30
         # print(a) name Error...
d1=Demo()
d1.m1()
d1.display()