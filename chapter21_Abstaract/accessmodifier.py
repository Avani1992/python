class Test:
    x=10 # public
    _y=20 # protected
    __z=30 # private
    def m1(self):
        print(Test.x) # 10
        print(Test._y) # 20
        print(Test.__z) # 30

t=Test()
t.m1()
print(Test.x) # 10
print(Test._y) # 20
#print(Test.__z) # AttributeError: type object 'Test' has no attribute '__z'... outside class private variable not possible..
print(t._Test__z) # 30