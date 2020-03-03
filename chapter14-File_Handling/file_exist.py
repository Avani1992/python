import  os,sys

fname=input("Enter File Name:")

if(os.path.isfile(fname)):
    print("File name is:",fname)
    print("File Content is:")
    with open(fname,"r") as f:
        f1=f.read()
        print(f1)
else:
    print("File not exist..")
    sys.exit(0) # system exit without executing rest of the program..
    
print("Hello")

