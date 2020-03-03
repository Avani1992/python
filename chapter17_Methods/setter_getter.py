class Car:
    def setName(self,name,model):
        self.name=name
        self.model=model
    def getName(self):
        return self.name,self.model

c1=Car()
c1.setName("Wagonr",2012)
print(c1.getName())
c2=Car()
c2.setName("i-10",2011)
r=c2.getName()
print(r)