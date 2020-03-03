class static1:
    a1=10
    def __init__(self):
        static1.a=100
        print("Constructor a= ",self.a)
    def m1(self):
        static1.b=200
        print("Instance method b= ",self.b)
    @classmethod
    def m2(cls):
        cls.c=300
        static1.c1=30
        print("Class method c=",cls.c)
        print("class method c1= ",static1.c1)
    @staticmethod
    def m3():
        static1.d=400
        print("Static method d= ",static1.d)

print(static1.__dict__)
print("Within class a1= ",static1.a1) # within class ,outside method
s1=static1() # 100
s1.m1() # call insstance method 200
static1.m2() # 300,30
static1.m3() # 400
print(static1.__dict__)

