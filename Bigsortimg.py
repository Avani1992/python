import re
unsorted=[31415926535897932384626433832795,1,3,10,3,5]
def bigSorting(unsorted):
  l1=list()
  while unsorted:
    current=unsorted[0]
    for j in unsorted:
      if(j<current):
        current=j
    l1.append(current)
    unsorted.remove(current)
  return l1
  
result=bigSorting(unsorted)
print(result)

#2.

import re
unsorted=[1,2,100,12303479849857341718340192371,3084193741082937,3084193741082938,111,200]
def bigSorting(unsorted):
  unsorted.sort()
  
  return (unsorted)
result=bigSorting(unsorted)
print(result)
