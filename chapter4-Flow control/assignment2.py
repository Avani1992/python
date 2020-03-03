n=int(input("Enter the Number: "))
# #
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(end=" ")
#     for j  in range(i):
#             print("*",end=" ")
#     print()
for i in range(1,n):
    for j in range(i):
        print(end=" ")
    for j in range(n-1):
        print("*",end=" ")
    print()
    n=n-1


#2.
# n=5
# for i in range(1,n+1):
#    print(" " * (n-i),end="")
#    print("* "*i)
# for i in range(1,n):
#     print(" "*(i),end="")
#     print("* "*(n-1))
#     n=n-1
#
#3.
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()