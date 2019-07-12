"""
2
12
1012
Sample Output

2
3
Explanation

The number 12 is broken into two digits, 1 and 2. When 12 is divided by either of those two digits, the remainder 
is 0 so they are both divisors.

The number 1012 is broken into four digits,1 ,0 ,2 ,4 and . 1012 is evenly divisible by its digits 1,0 ,1and 2, 
but it is not divisible by  0 as division by zero is undefined.


"""
n=12
def findDigits(n):
  l1=list()
  c=0
  m1=str(n)
  for i in range(0,len(m1)):
    l1.append(int(m1[i]))
  
  
  #print(t)
  for j in range(0,len(l1)):
    if(l1[j]!=0):
      if(n%l1[j]==0):
        c=c+1
    
  	
  return(c)
   
  
result=findDigits(n)
print(result)