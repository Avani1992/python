import copy
files = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}

def group_by_owners(files):
    value = list(files.values()) # ["Randy","Stan","Randy"]
    key = list(files.keys()) # ["Input.txt","Code.py","Output.txt"]

    l3 = list()
    l2 = copy.deepcopy(value) # l2=value.
    d = dict()
    l4 = list()
    for x in value:
        if (x not in l4): # to check x in list or not.
            l4.append(x)
            l3 = list()
            for y in range(0, len(l2)): # ["Randy","Stan","Randy"]
                if (x == l2[y]):  # if("Randy"=="Randy"),if("Randy"=="Stan"),if("Randy"=="Randy")

                    l3.append(key[y]) # append key[0],key[2] l3=["Input.txt","Output.txt"]
                else:
                    pass
            d[x] = l3 # d["Randy"]=["Input.txt","Output.txt"]

        else:
            pass

    return d
t=(group_by_owners(files))
print(t)