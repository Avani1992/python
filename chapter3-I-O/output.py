a,b,c=10,20,30
print(a,b,c,sep=":") # 10:20:30
print(a,b,c,sep="=") # 10=20=30

print("A,B,C is: ",end="") # end is used to concatenate next line with previous line...Ans: A,B,C is: 10,20,30
print(a,b,c,sep=",")

# name=input("Enter u r name: ") # Kuman
# age=int(input("Enter u r Age: ")) # 28
# print("Hello!!",name,".","U r Age is: ",age)  # Hello!! Kuman . U r Age is:  28 syntex: print(string,variable) here name and age is variable.

print("A value is:%i , B value is: %i" %(a,b)) # print("formatted string"  %(variable list)) .


 # print with replacement operator {}. .format() function used....
name = "Avani"
salary = 10000
place="Bangalore"
print("Hello {0} your salary is {1} and Your place  is : {2}".format(name, salary, place))
print("Hello {} your salary is {} and Your place  is : {}".format(name, salary, place))

print("Hello {x} your salary is {y} and Your place  is : {z}".format(x=name, y=salary, z=place))