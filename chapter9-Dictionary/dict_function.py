d=dict({1:"ABC",2:"BCD",'a':True,False:12.56})
d[12.67]='k'
print(d) # {1: 'ABC', 2: 'BCD', 'a': True, False:12.56, 12.67: 'k'}
del d[False]
print("After deleting: ",d) # {1: 'ABC', 2: 'BCD', 'a': True, 12.67: 'k'}
print("Length: ",len(d)) # 4
print("Value is: ",d.get(1)) # ABC
print("Value is: ",d.get(7)) # None
print("Value is: ",d.get(2,False)) # BCD
print("Value is: ",d.get(6,False)) # False . It is default value. If key is not in Dict it takes default value.
print("value is: ",d.setdefault(7,400)) # If key is not in dict it will add key-value in dict.
print("Dict is: ",d) # {1: 'ABC', 2: 'BCD', 'a': True, 12.67: 'k', 7: 400}
d.pop('a')
print("Pop :",d) # {1: 'ABC', 2: 'BCD', 12.67: 'k', 7: 400}
#d.pop('b')
#print("pop: ",d) # keyerror
d.popitem()
print("popitem :",d) # {1: 'ABC', 2: 'BCD', 12.67: 'k'}
k=d.keys()
print(k) # ([1, 2, 12.67])
v=d.values()
print(v) # dict_values(['ABC', 'BCD', 'k'])
print(d.items()) # dict_items([(1, 'ABC'), (2, 'BCD'), (12.67, 'k')])
d.update({5:500,7:700})
print("After update: ",d) #{1: 'ABC', 2: 'BCD', 12.67: 'k', 5: 500, 7: 700}
