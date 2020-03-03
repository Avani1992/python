with open("abc.txt","w") as f:
     f.write("prasanna\n")
     f.write("Software\n")
     f.write("Solutions\n")
     print("Is File Closed: ",f.closed) # False

print("Is File Closed: ",f.closed) # True. bcz outside 'with' block it automatically close the file...