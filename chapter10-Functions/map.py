#Eg: Without lambda

l=[1,2,3,4,5]
def doubleIt(x):
	return 2*x
l1=list(map(doubleIt,l))
print("Double without Lambda:",l1) #[2, 4, 6, 8, 10]
print()
# with lambda:-

l=[1,2,3,4,5]
l1=list(map(lambda x:2*x,l))
print("double with Lambda:",l1)	#[2, 4, 6, 8, 10]
print()

# Eg 2: To find square of given numbers

l=[1,2,3,4,5]
l1=list(map(lambda x:x*x,l))
print("square:",l1)	#[1, 4, 9, 16, 25]