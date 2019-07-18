a=[4,6,5,3,3,1]

def solve(x):
  x.sort()
  l1=list()
  l2=list()
  l3=list()
  l4=list()
  for a in range(0,len(x)):
    current=x[a]
    
    if(current in l3):
      pass
    else:
      sliced=x[a+1:]
      l3.append(current)
      l1.append(current)
      
      for j in sliced:
        if(abs(current-j)<=1):
          l1.append(j)
        else:
          pass
    
    l2.append(l1)
    l1=list()
    #print(l2)
  for i in l2:
    l4.append(len(i))
  
  return (max(l4)) 
  
t=solve(a)
#for k in t:
print(t) 