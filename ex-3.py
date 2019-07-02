x=[2,4]
y=[16,32,96]
l1=[]

def factor1(a,b):
  for i in a:
    for j in range(2,5):
      if((i*j)%4==0):
        l1.append(i*j)
  #print(l1)
  for k in l1:
    #print(k)
    for l in b:
      if(l%k!=0):
        l1.remove(k)
  print(l1)
          
    
factor1(x,y)
#print(t)

#2.

x=[1,2,3,4,5,1,2,1,2,1,3,2,2]
l1=[]
d={}
def migratory(a):
  for i in a:
    if(i in d.keys()):
      d[i]=d[i]+1
    else:
      d[i]=1
  for k in d:
    if(d[k]==max(d.values())):
      l1.append(k)
  if(len(l1)==1):
    print(l1)
  else:
    for j in range(0,len(l1)):
      current=l1[j]
      sliced=l1[j+1:]
      for l in sliced:
    	 if(current<l):
      	    print(current)
            break
      break     
migratory(x)