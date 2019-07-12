"""
https://www.google.com/url?q=https://www.hackerrank.com/challenges/permutation-equation/
problem&sa=D&source=hangouts&ust=1563014942688000&usg=AFQjCNEYpximszVtDTdfYuxhMbPsUbAaLQ
"""
p=[4,3,5,1,2]
def permutationEquation(p):
  j=1
  d={}
  l1=list()
  l2=list()
  for i in range(0,len(p)):
    d[j]=p[i]
    j=j+1
  #print(d)
  values=list(d.values())
  keys=list(d.keys())
  #print(values)
  for k in range(1,len(p)+1):
    l1.append(keys[values.index(k)])
  
  for l in l1:
    l2.append(keys[values.index(l)])
    
    
  return l2
result=permutationEquation(p)
print(result)