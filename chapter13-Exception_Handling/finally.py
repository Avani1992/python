import os
#1.If there is no exception.

# try:
#     print("Try block")
# except:
#     print("Except block")
#
# finally:
#     print("Finally block")
# o/p:
# Try block
# Finally Block

#2.If there is an exception raised but handled:
#
# try:
#     print("Statement-1")
#     print(10/0)
# except ZeroDivisionError as msg:
#     print("Error:",msg)
# finally:
#     print("Statement-2")
# print("Statement-3")

# o/p:
# Statement-1
# Error: division by zero
# Statement-2
# Statement-3

#3. If there is an exception raised but not handled:
#
# try:
#     print("Statement-1")
#     print(10/0)
# except TypeError as msg:
#     print("Error:",msg)
# finally:
#     print("Statement-2")
# print("Statement-3")
#
# o/p:
# Statement-1
# Statement-2
# ZerodivisionError

#4.
#
# try:
#     print("Statement-1")
#     os._exit(0)  # PVM shutdown. won't execute further code...finally block not executed..
#     print("Hello")
#
# except TypeError as msg:
#      print("Error:",msg)
# finally:
#      print("Statement-2")
# print("Statement-3")

# o/p;
# Statement-1

#5.

# try:
#     print("Statement-1")
#
#     print("Hello")
#
# except TypeError as msg:
#      print("Error:",msg)
# finally:
#     print(10/0)  # Error..abnormalTermination of prog.
#     print("Statement-2")
# print("Statement-3")

# o/p:
# Statement-1
# Hello
# ZerodivisionError