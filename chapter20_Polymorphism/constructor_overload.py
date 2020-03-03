class Test:
    def __init__(self):
        print('No-Arg Constructor')

    def __init__(self,a):
        print('One-Arg constructor')

    def __init__(self,a,b):
        print('Two-Arg constructor')

#t1=Test() # TypeError: __init__() missing 2 required positional arguments: 'a' and 'b'

#t2=Test(10) # TypeError: __init__() missing 1 required positional arguments: 'b'
t3=Test(10,20)

#2. Constructor overloading with default arguments..possible
# class Test:
#      def __init__(self,a=None,b=None,c=None):
#         print('Constructor with 0|1|2|3 number of arguments')
#
# t1=Test()
# t2=Test(10)
# t3=Test(10,20)
# t4=Test(10,20,30)

#3. constructor overloading with variable length argument possible..
#
# class Test:
#     def __init__(self, *a):
#         print('Constructor with 0|1|2|3 number of arguments')
#
#
# t1 = Test()
# t2 = Test(10)
# t3 = Test(10, 20)
# t4 = Test(10, 20, 30)
