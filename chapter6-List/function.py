#1.count()

l=[1,2,2,2,3,3,4]
# print(l.count(1)) # 1
# print(l.count(2)) # 3
# print(l.count(3)) # 2
# print(l.count(4)) # 1
# print(l.count(5)) # 0

#2. index()

print(l.index(1)) # 0
print(l.index(2)) # 1
print(l.index(3)) # 4
print(l.index(4)) # 6
# print(l.index(5)) # ValueError: 5 is not in list
print()

#3. append()

l.append("ABC")
l.append(True)
l.append(34.67)
print("List is: ",l) # [1, 2, 2, 2, 3, 3, 4, 'ABC', True, 34.67]

#4. insert()

l.insert(2,"BCD")
l.insert(15,False)
print("List after insert is: ",l) # [1, 2, 'BCD', 2, 2, 3, 3, 4, 'ABC', True, 34.67, False]

#5.extend()

l1=["Hello","How r u"]
l.extend(l1)
print(l) # [1, 2, 'BCD', 2, 2, 3, 3, 4, 'ABC', True, 34.67, False, 'Hello', 'How r u']

#6. remove()

l.remove(2)
print("After removing:",l) # [1, 'BCD', 2, 2, 3, 3, 4, 'ABC', True, 34.67, False, 'Hello', 'How r u']
l.remove('ABC')
print("After removing: ",l) # [1, 'BCD', 2, 2, 3, 3, 4, True, 34.67, False, 'Hello', 'How r u']

#7. pop()

l.pop()
print(l) # [1, 'BCD', 2, 2, 3, 3, 4, True, 34.67, False, 'Hello']
l.pop(2)
print(l) # [1, 'BCD', 2, 3, 3, 4, True, 34.67, False, 'Hello']
l.pop(6)
print(l) # [1, 'BCD', 2, 3, 3, 4, 34.67, False, 'Hello']

n=[]
#print(n.pop())  #   IndexError: pop from empty list

#8. reverse()

l.reverse()
print("Reverse is: ",l) # ['Hello', False, 34.67, 4, 3, 3, 2, 'BCD', 1]

#9. sort()
l2=[10,6,3,30,5,8,45]
l2.sort()
print("Sort is:",l2)

l3=["Dog","Apple","Elephant","Boat","Goat"]
l3.sort()
print(l3) # ['Apple', 'Boat', 'Dog', 'Elephant', 'Goat']


