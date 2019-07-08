"""
Given a range of numbered days[i...j],  and a number k, determine the number of days in the range that are beautiful. 
Beautiful numbers are defined as numbers where|i-reverse(i)|  is evenly divisible by k.
 If a day's value is a beautiful number, it is a beautiful day. Print the number of beautiful days in the range.
"""
def beautifulDays(i,j,k):
  l1=list()
  l2=list()
  l3=list()
  for p in range(i,j+1):
    no=p
    reverse=0
    while(no>0):
        r=no%10
        reverse=reverse*10+r
        no=no/10
        if(no==0):
          l1.append(reverse)
   
  for q in range(i,j+1):
    l2.append(q)
    
  for r in range(0,len(l2)):
    if(abs(l2[r]-l1[r])%k==0):
    if(abs(l2[r]-l1[r])%k==0):
      l3.append(l2[r])
  #print(l3)      
  return (len(l3))
