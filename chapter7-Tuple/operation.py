t1=(10,20,30)
t2=(40,50,60)
t3=t1+t2
print("Concatenation is: ",t3) #(10,20,30,40,50,60)
print("Multiplication is: ",t1*2) #(10,20,30,10,20,30)

print("Length of t1 is: ",len(t1)) # 3

t4=(55,10,65,20,10,30,10,40,30)
print("Count of 10 is: ",t4.count(10)) # 3
print("Count of 50 is: ",t4.count(50)) # 0
print("Index of 30 is: ",t4.index(30)) # 5
#print("Index of 50 is: ",t4.index(50)) # Value Error
print("Sorted tuple is: ",sorted(t4)) # [10, 10, 10, 20, 30, 30, 40, 55, 65]
print("DeCending Sorted tuple is: ",sorted(t4,reverse=True)) # [65, 55, 40, 30, 30, 20, 10, 10, 10]
print("Minimum is: ",min(t4)) # 10
print("Maximum is: ",max(t4)) # 65

t= ( x**2 for x in range(1,6))
print(type(t)) # generator
for x in t:
 print(x) # 1,4,9,16,25
