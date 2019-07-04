def kangaroo(x0,v0,x1,v1):
  for i in range(x0,10000):
    count1=0
    count2=0
    x0=x0+v0
    count1=count1+1
    x1=x1+v1
    count2=count2+1
    
    if(x0==x1 and count1==count2):
      print("YES")
      return
    else:
      pass
  print("NO")
      
    
kangaroo(4523, 8092, 9419 ,8076)