"""
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from  to  for three categories: problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet , and the rating for Bob's challenge to be the triplet .

Your task is to find their comparison points by comparing  with ,  with , and  with .

If , then Alice is awarded  point.
If , then Bob is awarded  point.
If , then neither person receives a point.
Comparison points is the total points a person earned.

Given  and , determine their respective comparison points.


"""
a=[2,2,1]
b=[3,2,2]

def compare1(x,y):
  l1=[]
  alice,bob=0,0
  for i in range(0,len(x)):
    if(x[i]-y[i]>0):
      l1.append(1)
    elif(x[i]-y[i]<0):
      l1.append(-1)
    else:
      pass
  print(l1)
  for m in l1:
    if(m==1):
      alice=alice+1
    elif(m==-1):
      bob=bob+1
      
  return(alice,bob)
t=compare1(a,b)
print(t)