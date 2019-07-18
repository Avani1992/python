"""
Monica wants to buy a keyboard and a USB drive from her favorite electronics store. The store has several models of
 each. Monica wants to spend as much as possible for the 2 items, given her budget.

Given the price lists for the store's keyboards and USB drives, and Monica's budget, find and print the amount of 
money Monica will spend. If she doesn't have enough money to both a keyboard and a USB drive, print -1 instead. 
She will buy only the two required items.

For example, suppose she has b=60 to spend. Three types of keyboards cost keyboard=[40,50,60] . 
Two USB drives cost USB=[5,8,12]. She could purchase a 40keyboards + 12 USB=52, or a 50Keyboards + 8USB=58. 
She chooses the latter. She can't buy more than 2 items so she can't spend exactly 60.
"""
a=[2,1]
b=[3,4]
c=7

def shopping(x,y,s):
  l1=[]
  for i in x:
    for j in y:
      if(len(x)==1 and len(y)==1 and i+j>=s):
        l1.append(-1)
      elif(i+j<=s):
        l1.append(i+j)
      else:
        l1.append(-1)
  print(max(l1))
  
shopping(a,b,c)  
