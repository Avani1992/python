class ToYoung(Exception):
    def __init__(self,arg):
        self.msg=arg
class ToOld(Exception):
    def __init__(self,arg):
        self.msg=arg

age=int(input("Enter age: "))

if age<18:
    raise ToYoung("To Young for mrg..Wait for sometime...")
elif age>60:
    raise  ToOld("To old for mrg..Now take rest...")
else:
    print("Suitable for mrg...Good luck..")