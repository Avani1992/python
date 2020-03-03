from sys import argv

sum=0
a=argv[1:]
for no in a:
    sum=sum+int(no)
print("Sum is: ",sum)