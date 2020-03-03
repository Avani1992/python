n1=int(input("Enter the First No: "))
n2=int(input("Enter the Second No: "))
n3=int(input("Enter the tird No: "))

if(n1<n2 and n1<n3):
    print("The Smallest No is: ",n1)
elif(n2<n3):
    print("The Smallest No is: ",n2)
else:
    print("The Smallest No is: ",n3)