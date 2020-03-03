# Write a program to take dictionary from the keyboard and print the sum of values?

d=eval(input("Enter the Dictionary data:"))
sum=0

for i in d.values():
    sum=sum+i
print("Sum is:",sum)

