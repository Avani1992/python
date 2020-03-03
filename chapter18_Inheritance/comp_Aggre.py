class Student:
    collegeName='PRASANNASOFT'
    def __init__(self,name):
        self.name=name

print(Student.collegeName) # Aggregation bcz without object calling possible...
s=Student(' Prasanna ')
print(s.name) # Composition bcz without object not possible..