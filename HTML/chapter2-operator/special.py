a=10
b=15
print("A is b: ",a is b) # false bcz both memory address is different. is compare the memory address.

c=10
print("a is c: ", a is c) # True
print(True is False) # False
print(True is True) # True
print(True is not False) # True

list1=["AB","BC","CD"]
list2=["AB","BC","CD"]
print(id(list1))
print(id(list2))
print("list check: ",list1 is list2) # False bcz both list value is same but address is different.
print(list1==list2) # True bcz value of both list is same.


d="Python is easy to learn"
print("python" in d) # False we used "Python " not "python"
print("pyton" not in d) # True
print(3/2*4+3+2.0**3-2 )