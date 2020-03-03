f=open("abc1.txt","w")
f.write("Python\n")
f.write("Java\n")
f.writelines(["Pearl\n","Ruby\n","C++\n"])
f.close()

# f1=open("abc.txt","w") # overriddenn with c. now only c is there...
# f1.write("c")

f1=open("abc1.txt","a") # appended to the file...
f1.write("C")

print("Write_file....")