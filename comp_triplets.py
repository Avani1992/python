a=[2,2,1]
b=[3,2,2]

def compare1(x,y):
  l1=[]
  alice,bob=0,0
  for i in range(0,len(x)):
    if(x[i]-y[i]>0):
      l1.append(1)
    elif(x[i]-y[i]<0):
      l1.append(-1)
    else:
      pass
  print(l1)
  for m in l1:
    if(m==1):
      alice=alice+1
    elif(m==-1):
      bob=bob+1
      
  return(alice,bob)
t=compare1(a,b)
print(t)