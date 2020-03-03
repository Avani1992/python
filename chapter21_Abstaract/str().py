class Test:
    def m1(self):
        print("Hello...")
    # def __str__(self): original object class method
    #     return <__main__.classname object at hashcode>

    def __str__(self): # overided object class method
        return "object str() method override..."

t=Test()
t.m1() # Hello
#print(t) # <__main__.Test object at 0x01259CD0>...class name with hashcode...to overcome this problem we have to override __str__() method of object class...
print(t) # object str() method override...

