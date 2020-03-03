# def factorial(n):
# 	if n==0:
# 		result=1
# 	else:
# 		result=n*factorial(n-1)
# 	return result
# print("Factorial of 4 is :",factorial(4))
# print("Factorial of 5 is :",factorial(5))

def fa(n):
	if(n==0 or n==1):
		return 1
	else:
		return n*fa(n-1)
p=fa(5)
print(p)