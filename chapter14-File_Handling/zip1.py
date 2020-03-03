from zipfile import *
#  write

# f=ZipFile("Emp.zip","w",ZIP_DEFLATED)
# f.write("read_")
# f.write("write_file.py")
# f.close()
# print("Zip Completed...")

# read

f=ZipFile("Emp.zip","r",ZIP_STORED)
names=f.namelist()
for i in names:
    print("File name :",i)
    f=open(i,"r")
    data=f.read()
    print(data)