a=[1,3,5,9,7]

def mi_max_sum(x):
  
  max1=max(x)
  min1=min(x)
  max_sum=0
  min_sum=0
  for i in x:
    if(i==max1):
      pass
    else:
      min_sum=min_sum+i
  
    if(i==min1):
      pass
    else:
      max_sum=max_sum+i
  
      
  return (min_sum,max_sum)
  
t=mi_max_sum(a)
print(t)