l1=[1,2,3,4,5,7,8,10]

for i in range(0,len(l1)):
    if(i+1==len(l1)):
        break
    elif(l1[i]+1!=l1[i+1]):
        print(l1[i]+1)
