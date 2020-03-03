l1=[23 ,13 ,25 ,29 ,33 ,19 ,34 ,45 ,65 ,67]

l2=list()
l3=list()

for i in range(0,len(l1)):
    if(i+1<len(l1)):
        if(l1[i]>l1[i+1]):

            l2.append(l1[i+1])
            if(len(l2)>1):
                l3.append(l1[i])

        if(i+1==len(l1)-1):
            l3.append(l1[i+1])

print(l2)
print(l3)
