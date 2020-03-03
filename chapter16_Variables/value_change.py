class Test:
     def __init__(self):
         self.a=10
         self.b=20

t1=Test()
t1.a=888 # change value
t1.b=999
t2=Test()
print('t1:',t1.a,t1.b) # t1: 888 999
print('t2:',t2.a,t2.b) # t2: 10 20
print()

del t2.b # delete b of t2 object
print('t1:',t1.a,t1.b) # t1: 888 999
print('t2:',t2.a) # 10