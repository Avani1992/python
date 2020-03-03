# f=open("read_write.txt","w")
# print("File Name is: ",f.name) # read_write.tex
# print("File Mode: ",f.mode) # w
# print("Is File Readable:  ",f.readable()) # False
# print("Is File Writable:  ",f.writable()) # True
# print("Is File Closed : ",f.closed) # False
#
# #  Write Function....
#
#
# f.write("Hello\n")
# f.write("How r u???\n") # only string possible. one line argument.
# l=["Python\n","is\n","very\n","easy"]
#
# f.writelines(l) # we can pass list,tuple and set.
# f.close()
# print("Is File Closed : ",f.closed) # True

# Read Function....

f1=open("read_write.txt","r")
#1.
#print(f1.read()) # read the whole file..

#2.
#print(f1.read(4)) # Hell. read only 4 character from indicating pointer..
#print(f1.read()) # start reading from after 4 th character bcz first 4 character read in previous print..

#3.
#print(f1.readline()) # Hello...
#print(f1.readlines()) # return list of all data....['Hello\n', 'How r u???\n', 'Python\n', 'is\n', 'very\n', 'easy']
