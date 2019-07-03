"""
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. In the diagram below, the red region denotes his house, where  is the start point, and  is the endpoint. The apple tree is to the left of his house, and the orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point , and the orange tree is at point .

Apple and orange(2).png

When a fruit falls from its tree, it lands  units of distance from its tree of origin along the -axis. A negative value of  means the fruit fell  units to the tree's left, and a positive value of  means it falls  units to the tree's right.

Given the value of  for  apples and  oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range )?


"""

apples=[2,5,6]
oranges=[-5,-2,2]

def countApplesAndOranges(s, t, a, b, apples, oranges):
  l1=[]
  l2=[]
  for i in apples:
    l1.append(i+a)
  for j in oranges:
    l2.append(j+b)
  #print(l1)
  #print(l2)
  for k in l1:
    if(k in range(s,t)):
      pass
    else:
      l1.remove(k)
  print(len(l1))
  for p in l2:
    if(p in range(s,t)):
      pass
    else:
      l2.remove(p)
  print(len(l2))
  
  
countApplesAndOranges(8,12,5,12,apples,oranges)