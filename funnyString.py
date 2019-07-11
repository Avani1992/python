s="bcxz"
def funnyString(s):
  l1=list()
  t=len(s)
  l2=list()
  l3=list()
  l5=list()
  for k in range(0,t):
    j=k+1
    if(j==t+1):
      break
    else:
      l1.append(s[k:j])
      
  for p in l1:
    l2.append(ord(p))
    
  for q in range(0,len(l2)):
    if(q+1==len(l2)):
      break
    else:
      l3.append(abs(l2[q]-l2[q+1]))
  l4=l3
  l2.reverse()
  for q in range(0,len(l2)):
    if(q+1==len(l2)):
      break
    else:
      l5.append(abs(l2[q]-l2[q+1]))
      
      
  if(l4==l5):
    return "Funny"
  else:
    return "Not Funny"

  
    
 
  
result=funnyString(s)
print(result)