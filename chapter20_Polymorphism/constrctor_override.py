class Parent:
    def __init__(self):
        print("Parent constructor...")

class Child(Parent):
    def __init__(self):
        super().__init__() # Parent constructor calling...
        print("Child constructor...")

c=Child()