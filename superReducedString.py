zz tqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh

tqauhujtmxnsbzpykwlvpfyqijvdhuhirdmuxiobyvxupqwydkpbxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh

tqauhujtmxnsbzpykwlvpfyqijvdhuhirdmuxiobyvxupqwydkpbxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh

s="zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh"
def superReducedString(s):
    l1=list()
    s1=""
    for i in s:
      if(len(l1)==0):
        l1.append(i)
      else:
        if(i==l1[-1]):
          l1.pop()
        else:
          l1.append(i)
          #print(l1)
      
    if(len(l1)>0):
      for i in l1: 
        s1=s1+i
      return (s1)
    else:
      return "Empty String"
  
result=superReducedString(s)
print(result)