import copy
files = { 'Input.txt': 'Randy', 'Code.py': 'Stan','Output.txt': 'Randy'}
value=list(files.values())
key=list(files.keys())

l3=list()
l2=copy.deepcopy(value)
d=dict()
l4=list()
for x in value:
    if(x not in l4):
        l4.append(x)

        l3 = list()
        for y in range(0,len(l2)):
            if(x==l2[y]):
                #print("x=",x,"y=",l2[y])
                l3.append(key[y])
            else:
              pass

        d[x]=l3

    else:
        pass
print(d)






