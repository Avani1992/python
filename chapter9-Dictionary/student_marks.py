#Write a program to accept student name and marks from the keyboard and creates a dictionary.
# Also display student marks by taking student name as input?

n=int(input("Enter No of Student:"))
i=1
d=dict()
while(i<=n):
    name=input("enter Student name:")
    marks=int(input("Enter Marks:"))
    d[name]=marks
    i=i+1
while True:
    name=input("Enter student name to see the Marks:")
    marks=d.get(name,-1)
    if(marks==-1):
        print("Student not found..")
    else:
        print(name ,"Marks is:",marks)
    choice=input("R u want to continue")
    if(choice=='No'):
        break