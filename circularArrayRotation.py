import copy
a=[1,2,3]
queries=[0,1,2]
def circularArrayRotation(a, k, queries):
    a1=list()
    a2=list()
    right_sliced=a[0:len(a)-k]
    left_sliced=a[len(a)-k:]
    
    a1.append(left_sliced+right_sliced)
    
    for i in a1:
     
        for k in queries:
             for j in range(k,len(i)):
              a2.append(i[j])
              break
    
 
    return a2
result=circularArrayRotation(a, 2,queries)
print(result)