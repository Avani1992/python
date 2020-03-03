s=input("enter String: ")

#1.
print("Reverse String is: ",s[::-1])

#2.
print()
l=len(s)
s1=""
while(l>0):
    s1=s1+s[l-1]
    l=l-1
print("Reverse String is: ",s1)

#3.
print()
s2=''.join(reversed(s))
print("Reverse String is: ",s2)