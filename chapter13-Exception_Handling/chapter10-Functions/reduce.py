from functools import *
# l=[10,20,30,40,50]
# result=reduce(lambda x,y:x+y,l)
# print(result) # 150
# print()
#
#
# result=reduce(lambda x,y:x*y,l)
# print(result) #12000000
# print()
#
#
#
# result=reduce(lambda x,y:x+y,range(1,101))
# print(result) #5050


def swap(x, y):
    temp = x;
    x = y;
    y = temp;
    print(x,y)


# Driver code
x = 2
y = 3
swap(x, y)
print(x)
print(y)
