s={}
print(s) # {}
print(type(s)) # dict

s=set()
print(s) # set()
print(type(s)) # set

s1={10,20,10,30,40}
s1.add(50)
print("After Add: ",s1) #  {40, 10, 50, 20, 30}
# s1.update(100,200)
#print("After Add: ",s1) # TypeError: 'int' object is not iterable

s1.update([100,200]) # we can update only list,tuple,range ..iterable objects only updated
print("After Update: ",s1) # {100, 40, 200, 10, 50, 20, 30}
s2=s1.copy()
print("Copy is: ",s2) # {50, 100, 20, 40, 10, 30, 200} clone copy. both address is different. modification in s1 not affect to s2 and viceversa..

s1.pop()
print("After pop from s1: ",s1) # {40, 200, 10, 50, 20, 30}
print("After pop from s1 s2 is: ",s2) # {50, 100, 20, 40, 10, 30, 200}

#s1.remove(100)
print("After remove from s1: ",s1) # keyError: 100 not in set
s1.remove(50)
print("After remove from s1: ",s1) # {40, 200, 10, 20, 30}

s1.discard(30)
print("After discard from s1: ",s1) # {40, 200, 10, 20}

s1.discard(50)
print("After discard from s1: ",s1) # {40,200,10,20} No Error

s3={10,20,30}
s4={40,30,50,60,50}

print("Union is: ",s3.union(s4)) # {50, 20, 40, 10, 60, 30}
print("Union is: ",s3 | s4) # {50, 20, 40, 10, 60, 30}

print("Intersection is: ",s3.intersection(s4)) # {30}
print("Intersection is: ",s3 & s4)  # {30}

print("Difference is: ",s3.difference(s4)) # {10,20}
print("Difference is:",s3-s4) # {10,20}

print("Symettric difference: ",s3.symmetric_difference(s4)) # {40,10,20,50,60}
print("Symettric difference: ",s3 ^s4) # {40,10,20,50,60}









