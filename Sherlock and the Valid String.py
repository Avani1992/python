"""
Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will 
occur the same number of times. Given a string s, determine if it is valid. If so, return YES, otherwise return NO.
"""
s="aabbc"
def isValid(s):
  d={}
  l1=list()
  l2=list()
  l3=list()
  if(len(s)==1):
    return "YES"
  else:
    for i in s:
      if(i in d):
        d[i]=d[i]+1
      else:
        d[i]=1
    print(d)
    
  for j in d.values():
     l1.append(j)
  current=l1[0]
  for k in range(0,len(l1)):
    sliced=l1[k+1:]
    for p in sliced:
      if(current==p):
        l2.append(current)
      elif(current>p or current<p):
        l3.append(p)
    break
  print(l3) 
  if(len(l2)==(len(s)/2)):
      return "YES"
  if(len(l3)>=2):
      return "No"
  else:
    for q in l3:
      if(q==(current+1) or q==(current-1) or q==1):
          return "Yes"
      else:
          return "No"
    
  
result=isValid(s)
print(result)
