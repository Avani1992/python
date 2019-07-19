import re
s="AUzs-nV"
def minimumNumber(n, password):
    flag = 0
    l1=list()
    while True:   
      if not re.search("[a-z]", password): 
         l1.append(1)
      if not re.search("[A-Z]", password): 
           l1.append(1)
      if not re.search("[0-9]", password): 
           l1.append(1)
      if not re.search("[!@#$%^&*()-+]", password): 
           l1.append(1)
      print(l1) 
      if (n<=6):
         if(n==6 and len(l1)==3):
          return (len(l1))
         if(n==6 and len(l1)==2):
          return (len(l1))
         if(n==6 and len(l1)==1):
          return (len(l1))
        
         if(n==5 and len(l1)==3):
          return (len(l1))
         if(n==5 and len(l1)==2):
          return (len(l1))
         if(n==5 and len(l1)==1):
          return (len(l1))
         if(n==5 and len(l1)==0):
          return(6-n)
         if(n==4 and len(l1)==3):
          return (len(l1))
         if(n==4 and len(l1)==2):
          return (len(l1))
         if(n==4 and len(l1)==1):
          return (len(l1)+1)
         if(n==4 and len(l1)==0):
          return(6-n)
         if(n==3):
          return (6-n)
         else:
          return (6-n)
          break
      if(n>=7):
            return(len(l1))
      else:
          return 0
result=minimumNumber(len(s), s)
print(result)