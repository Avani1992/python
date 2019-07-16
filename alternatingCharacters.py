"""
You are given a string containing characters A and B only. Your task is to change it into a string such that 
there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the 
string.

Your task is to find the minimum number of required deletions.

For example, given the string S="AABAAB", remove an A at positions 0 and 3 to make S=ABAB in 2 deletions.
"""
s="AAAB"
def alternatingCharacters(s):
  l1=list()
  l2=list()
  d=0
  for i in s:
    l1.append(i)
  current=l1[0]
  sliced=l1[1:]
  l2.append(current)
  for j in sliced:
    if(current==j):
      d=d+1
      pass
    else:
      l2.append(j)
      current=j
  print(l2)
  return(d)
  
result=alternatingCharacters(s)
print(result)