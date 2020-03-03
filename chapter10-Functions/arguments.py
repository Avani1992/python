#1. positional argument

def f1(name,age):
    print("Hello",name,"U r age is:",age)
f1("Avani",28)
f1("Kuman") # Throw error. one positinal argument-age missing.
print()
#2. Keyward argument

def f1(name,age):
    print("Hello",name,"U r Age is: ",age)
f1(name="Avani",age=28) # we can't pass positional argument after keyword argument.def f1(name,age,place) f1(name="Avani",age=28,"Bangalore")
f1(age=29,name="Kuman")
print()
#3. Default argument

def f1(name="Avani"): # we can't pass non-default argument after default argument. eg. def f1(name="Avani",age).
    print("Hello",name)
f1() # Hello Avani .If don't pass any argument it take default argument.
f1("Kuman") # Hello Kuman
print()
#4. Variable length Argument
def sum(*n):
	total=0
	for n1 in n:
		total=total+n1
	print("The Sum=",total)

sum()
sum(10)
sum(10,20)
sum(10,20,30,40)
print()

#5. keyward variable length argument

def display(**kwargs):
    for k,v in kwargs.items(): # store  inside dictionary .
    	print(k,"=",v)
display(n1=10,n2=20,n3=30)

