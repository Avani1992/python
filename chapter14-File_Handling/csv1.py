import csv
# #1. writer()
# f=open("Emp1.csv","w",newline='')
# w=csv.writer(f)
# w.writerow(["Eno","Ename","Sal"])
# n=int(input("Enter the No:"))
# for i in range(n):
#     eno=int(input("Enter Eno:"))
#     ename=input("Enter Ename:")
#     esal=int(input("Enter Esal:"))
#     w.writerow([eno,ename,esal])
# f.close()
# print("Data Entered...")

#2. reader()

f=open("Emp1.csv","r")
r=csv.reader(f)
for i in r:
    for  j in i:
        print(j,end='   ')
    print()