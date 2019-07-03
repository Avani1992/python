"""
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array 
of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, n=7 there are  socks with colors ar=[1,2,1,2,3,1,2] . There is one pair of color  and one of color . 
There are three odd socks left, one of each color. The number of pairs is 2.


"""

a=[10,20,30,10,20,50,10,50,30,50]

def sockMerchant(x):
  d={}
  l1=[]
  for i in x:
    if(i in d.keys()):
      d[i]=d[i]+1
    else:
      d[i]=1
  print(d)  #  mo. of elememts how mamy times.
  for k in d:
    if((d[k])>=2):
      l1.append((d[k])/2)  # total evem mo. of values
  print("Total pair of Socks: ",sum(l1))
  
sockMerchant(a) 