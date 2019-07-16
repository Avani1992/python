"""
Append a character to the end of string  p at a cost of 1 dollar.
Choose any substring of p and append it to the end of p at no charge.
Query 0: We start with s="abcd" and p="".

Append character 'a' to p at a cost of 1 dollar, p='a'.
Append character 'b' to p at a cost of 1 dollar, p='ab'.
Append character 'c' to p at a cost of 1 dollar, p='abc'.
Append character 'd' to p at a cost of 1 dollar, p='abcd'.
Because the total cost of all operations is 1+1+1+1 dollars, we print 4 on a new line.

Query 1: We start with s="abab" and p="".

Append character 'a' to p at a cost of 1 dollar, p='a'.
Append character 'b' to p at a cost of 1 dollar, p='ab'.
Append substring  'ab'to p at no cost, .
Because the total cost of all operations is 1+1 dollars, we print 2 on a new line.
"""

s="abab"
def stringConstruction(s):
  
  p=list()
  c=0
  for i in s:
    if(i in p):
      p.append(i)
    else:
      c=c+1
      p.append(i)
  print(p)
  return c
      
  
  
result=stringConstruction(s)
print(result)