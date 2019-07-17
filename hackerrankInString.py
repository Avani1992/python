"""
2
hereiamstackerrank
hackerworld

Sample Output 0

YES
NO
Explanation 0

We perform the following q=2 queries:
1.s=hereiamstackerrank
 
The characters of hackerrank are bolded in the string above. Because the string contains all the characters in 
hackerrank in the same exact order as they appear in hackerrank, we print YES on a new line.
 
 2. s=hackerworld
 
 does not contain the last three characters of hackerrank, so we print NO on a new line.
"""
s="hacakaeararanaka"
s1="hackerrank"
def hackerrankInString(s):
  s2=""
  j=0
  for i in range(0,len(s)):
    if(j==len(s1)):
      break
    else:
      if(s[i]==s1[j]):
        s2=s2+s1[j]
        #print(s2)
        j=j+1
        #print(j)
      else:
        i=i+1
        #print(i)
        
  print(s2)
  if(s2==s1):
    return "YES"
  else:
    return "NO"
  
result=hackerrankInString(s)
print(result)