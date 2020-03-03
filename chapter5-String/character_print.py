s=input("Enter Name: ")
i=0
# for x in s:
#     print("Character at positive index  {} and Negative index  {} is {} ".format(i,i-len(s),x))
#     i=i+1
#
# for x in range(len(s)):
#     print(s[x])

l=len(s)
# while(l>0):
#     print("Forward Direction: ",s[i])
#     i=i+1
#     l=l-1
print("Backward...")
j=len(s)-1
while(l>0):
    print("Backward Direction: ",s[j])
    l=l-1
    j=j-1