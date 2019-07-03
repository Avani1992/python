"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four 
of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated
 long integers.

For example,arr=[1,3,5,7,9] . Our minimum sum is  1+3+5+7=16 and our maximum sum is 3+5+7+9=24 . We would print

Ans=16 24
"""
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