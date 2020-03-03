s="0000101"
c=0
for i in range(0,len(s)):
    if(s[i]=='1'):
        c=i

if(c>0):
    print(c)
else:
    print(-1)

