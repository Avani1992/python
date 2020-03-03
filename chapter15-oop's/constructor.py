class const:

    def __init__(self,sname,sage):
        self.sname=sname
        self.sage=sage
    def sdetail(self):
        print("Student Name is {} , Student age is {} ".format(self.sname,self.sage))

c1=const("Avani",25)
c2=const("Kuman",26)
c1.sdetail()
c2.sdetail()