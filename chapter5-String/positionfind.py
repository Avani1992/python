# Program to display all positions of substring in a given main string ..

Main=input("Enter Main String: ")
sub=input("Enter SubString: ")

flag=False
pos=-1
n=len(Main)
while True:
    pos=Main.find(sub,pos+1,n)
    if pos==-1:

        break
    print("Found at position",pos)
    flag=True
if flag==False:
    print("Not Found")

#2.
s=input("Enter Some String:")
print("Characters at Even Position:",s[0::2])
print("Characters at Odd Position:",s[1::2])
