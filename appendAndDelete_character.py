"""
You have a string of lowercase English alphabetic letters. You can perform two types of operations on the string:


Append a lowercase English alphabetic letter to the end of the string.
Delete the last character in the string. Performing this operation on an empty string results in an empty string.
Given an integer k, , and two strings,s  and t, determine whether or not you can convert s to t by performing 
exactly k of the above operations on s. If it's possible, print Yes. Otherwise, print No.
"""

s="aba"
t="aba"

def appendAndDelete(s, t, k):
  l1=list()
  l2=list()
  
  c=0
  if(len(s)>=len(t)):
    for i in range(0,len(t)):
      if(s[i]==t[i]):
        c=c+1
      else:
        break
  else:
    for i in range(0,len(s)):
      if(s[i]==t[i]):
        c=c+1
      else:
        break
    
  difference_s=len(s)-c
  difference_t=len(t)-c
 # print(difference_s)
  #print(difference_t)
  l3=list()
  l1=s[0:c]
  #print(l1)
  l2=t[c:]
  #print(l2)
  l3=l1+l2
  #print(l3)
  if(t==l3 and k>=(difference_s+difference_t)):
    return ("yes")
  else:
    return ("no")
  
result=appendAndDelete(s, t, 7)
print(result)