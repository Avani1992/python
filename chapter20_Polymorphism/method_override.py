class Parent:
    def Car(self):
        print("Let's buy a Car")
    def Color(self):
        print("Buy White color Car")
class Child(Parent):
    def Color(self):
        super().Color()  # Parent method calling...
        print("Want to buy Royal Blue color Car")

c=Child()
c.Car()
c.Color()