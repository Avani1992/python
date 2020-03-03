n=int(input("Enter the Number: "))
# #  # 1.
# for i in range(1,n+1):
#     for j in range(i):
#
#         print("1",end=" ")
#     print()
#
#  # OR
# n=5
# for i in range(1,n+1):
#     print("* " * i)


# print()
#
# # # 2.
# #
# k=2*n -2
#
# for i in range(1,n+1):
#     for j in range(k):
#         print(end=" ")
#     k=k-2
#     for j in range(0,i):
#         print("1",end=" ")
#     print()

# print()
#
#  #3.
#
k=n
m=n
l=5

#
# for i in range(n):
#     for j in range(n):
#         print(end=" ")
#     n=n-1
#     for j in range(0,i):
#         print("*",end=" ")
#     print()

# #4.
#
# for i in range(n-1):
#     for j in range(k-l):
#         print(end=" ")
#     l=l-1
#     for j in range(m-2):
#         print("*",end=" ")
#     m=m-1
#     print()

#5.
#
# for i in range(n):
#
#     for j in range(n):
#         print("1",end=" ")
#     n=n-1
#     print()
# print()
#
# #6.
#
k=0
for i in range(n):
    for j in range(k):
        print(end=" ")
    k=k+2
    for j in range(n):
        print("1",end=" ")
    n=n-1
    print()