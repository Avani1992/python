class orange:
    def __init__(self):
        self.a=100 # instance variable using self in constructor
        #del self.a
    def m1(self):
        self.b=200 # instance variable using self in instance method..


o1 = orange()
o1.c=300 # instance variable using object reference
o1.m1()
print(o1.a) # 100
print(o1.b) # 200
print(o1.c) # 300
print(o1.__dict__) # {'a': 100, 'c': 300, 'b': 200}


