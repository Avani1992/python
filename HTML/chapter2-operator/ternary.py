a=int(input("Enter first value: "))
b=int(input("Enter second value: "))
c=int(input("Enter third value: "))

min= a if a<b and a<c else b if b<c else c
print("Min is: ",min)