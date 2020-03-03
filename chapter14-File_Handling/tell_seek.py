# #1. tell()
#
# f=open("abc.txt","r")
# print(f.tell()) # 0(index)
# print(f.read(2)) #Pr
# print(f.tell()) #2
# print(f.read(3))  #asa
# print(f.tell()) # 5

# 2. seek()
# data="Java is easy to learn"
# f=open("seek.txt","w")
# f.write(data)
with open("seek.txt","r+") as f1:
    print("Current position of pointer: ", f1.tell()) # 0
    text=f1.read()
    print("Data is: ",text) # Java is easy to learn
    print("Current position of pointer: ", f1.tell()) # 21
    f1.seek(8) #  jump pointer to 8 th position..
    print("Current position of pointer: ", f1.tell()) # 8
    f1.write("difficult")
    f1.seek(0) # jump pointer to 0th position.
    t1=f1.read()
    print("String is after update is: ",t1)



