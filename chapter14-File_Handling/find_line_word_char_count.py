import os,sys

fname=input("Enter File name:")
if(os.path.isfile(fname)):
        f1=open(fname,"r")
        lcount,wcount,ccount=0,0,0

        for line in f1:
            lcount=lcount+1
            ccount=ccount+len(line)
            sword=line.split()
            wcount=wcount+len(sword)
        print("Line count is: ",lcount)
        print("Word count is: ",wcount)
        print("character count is: ",ccount)
else:
    print("File not Exist...")
    sys.exit(0)

# import os,sys
# fname=input("Enter File Name: ")
# if os.path.isfile(fname):
#      print("File exists:",fname)
#      f=open(fname,"r")
# else:
#      print("File does not exist:",fname)
#      sys.exit(0)
# lcount=wcount=ccount=0
# for line in f:
#      lcount=lcount+1
#      ccount=ccount+len(line)
#      words=line.split()
#      wcount=wcount+len(words)
# print("The number of Lines:",lcount)
# print("The number of Words:",wcount)
# print("The number of Characters:",ccount)