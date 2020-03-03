import  time
from instance_method import *
import  sys


class Test:
     def __init__(self):
         print("Object Initialization...")
     def __del__(self):
         print("Fulfilling Last Wish and performing clean up activities...")

# 1.
# t1=Test()
# time.sleep(5)
# t1=None   # object reference free.pointing nothing..Call __del__
# time.sleep(5)
# print("End of application")

#2.

# t1=Test()
# t2=t1
# t3=t2
# del t1   # still t2,t3 remaining
# time.sleep(5)
# print("object not yet destroyed after deleting t1")
# del t2 # still t3 remaining..
# time.sleep(5)
# print("object not yet destroyed even after deleting t2")
# print("I am trying to delete last reference variable...")
# del t3 # all object reference deleted..call __del__

#3.

list=[Test(),Demo(),Test()]   # in list 3 class objects r there. 3 time constructor calling..
#del list   # whole list delete. one by one delete and call __del__ 3 times. In Demo class no __del__ there..
# time.sleep(5)
print("End of application")


list1=list
# t2=t1
# t3=t2
print("Reference count=",sys.getrefcount(list)) # list,list1,self. total=3
# d1=Demo()