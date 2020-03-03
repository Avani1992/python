# d={1:"ABC",'a':"BCD",False:1}
# d[4]=12.45
# print(d)
# #print(d[10]) # keyerror
# print(d[1]) # ABC

#Write a program to enter name and percentage marks in a dictionary and display information on the screen
rec={}
n=int(input("Enter number of students: "))
i=1
while i <=n:
    name=input("Enter Student Name: ")
    marks=input("Enter % of Marks of Student: ")
    rec[name]=marks
    i=i+1
print(rec)