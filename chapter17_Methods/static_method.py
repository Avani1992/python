class PrasannaMath:

     @staticmethod
     def add(x,y):  # x, y is local variable...
         print('The Sum:',x+y) # 30

     @staticmethod
     def product(a,b):
        print('The Product:',a*b) # 200

     @staticmethod
     def average(x,y):
         print('The average:',(x+y)/2) # 15.0

PrasannaMath.add(10,20)
PrasannaMath.product(10,20)
PrasannaMath.average(10,20)