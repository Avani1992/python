a=[2,4]
b=[16,32,96]
l1=[]
def solve(x,y):
  temp=[]
  for i in a:
    for j in range(1,7):
      l1.append(i*j)
  for j in l1:
    for k in a:
      if(j%k!=0):
        l1.remove(j)
  for l in range(0,len(l1)):
    current=l1[0]
    sliced=l1[l+1:]
    for m in sliced:
      if(current==m):
        l1.remove(current)
      else:
        pass
  for p in b:
    for q in l1:
      if(p%q==0):
        pass
      else:
        l1.remove(q)
  return l1
t=solve(a,b)
print((t))          
    