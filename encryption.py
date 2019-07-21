import math
s="iffactsdontfittotheorychangethefacts"
def encryption(s):
  s1=""
  l1=list()
  l=len(s)
  print(l)
  l1=int(math.sqrt(l))
  print(l1)
  
  r=l1
  c=l1
  s2=""
  l2=list()
  if(r*c<l):
    r=r+1
    c=c+1
    d=c
    k=0
    for i in range(0,r):
     
      for j in range(k,c):
          #print(j)
          if(j>len(s)-1):
            break
          else:
            s1=s1+s[j]
            #print(s1)
            if(j==c):
              break
              
      l2.append(s1)
      s1=""
      print(l2)
      k=c
      c=c+d
  else:
        d=c
        k=0
        s2=""
        for i in range(0,r):
     
          for j in range(k,c):
            #print(j)
            if(j>len(s)-1):
              break
            else:
              s1=s1+s[j]
              #print(s1)
              if(j==c):
                break
          
          l2.append(s1)
          s1=""
          print(l2)
          k=c
          c=c+d
    
  
  s=""
  l4=list()
  l3=[char for char in l2[0]]
  for ele in l2[1:]:
    i=0
    for char in ele:
   
      l3[i]=l3[i]+char
      i=i+1
    #print(l4)
    
  

  for k in l3:
    s=s+" "+k
    #print(s) 
  return s
      
  
result=encryption(s)
print(result)