"""
Fill set s with 5x5 elememts amd primt all diagomal elememts from that set((0,0)(1,1)..(5,5))
"""

s=set()
for i in range(0,5):
  
  for j in range(0,5):
    
    s.add((i,j))
#print(s)

for pair in s:
  p,k=pair
  if(p==k):
	print(pair)
  		

# each (i,j) pair im a set

#2. 
arr=[(1,2,3),(4,5,6),(9,8,9)]
def diagonalDifference(arr):
  sum=0
  sum1=0
  for i in range(0,len(arr)):
    j=i
    sum=sum+arr[i][j]
  print(sum)
  
  i=len(arr)-1
  for j in range(0,len(arr)):
    sum1=sum1+arr[i][j]
    i=i-1
  print(sum1)
  
  difference=(abs(sum-sum1))
  return difference
result=diagonalDifference(arr)
print(result)