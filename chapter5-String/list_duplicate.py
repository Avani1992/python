l1=["ABC","BCD","CBD"]
l2=["ABC","CBD","DEF"]
for x in l1:
    if(x in l2):
        l2.remove(x)

l3=l1+l2
print(l3)