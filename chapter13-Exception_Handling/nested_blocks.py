#1.
# try:
#      print("outer try block")
#      try:
#          print("Inner try block")
#          print(10/0)
#      except ZeroDivisionError:
#          print("Inner except block")
#      finally:
#         print("Inner finally block")
# except:
#      print("outer except block")
# finally:
#      print("outer finally block")

# o/p:
# outer try block
# Inner try block
# Inner except block
# Inner finally block
# outer finally block

#2.
#
# try:
#     print("Statement-1")
#     print(10/0)
#     try:
#         print("Statement-2")
#     except TypeError:
#         print("Statement-3")
#     finally:
#         print("Statement-4")
# except:
#     print("Statement-5")
# finally:
#     print("Statement-6")
#
# print("statement-7")

# o/p:
# Statement-1
# Statement-5
# Statement-6
# statement-7

#3.

#
# try:
#     print("Statement-1")
#
#     try:
#         print("Statement-2")
#         print(10/0)
#     except TypeError:
#         print("Statement-3")
#     finally:
#         print("Statement-4")
# except:
#     print("Statement-5")
# finally:
#     print("Statement-6")
#
# print("statement-7")
#
# o/p:
# Statement-1
# Statement-2
# Statement-4
# Statement-5
# Statement-6
# statement-7

# #4.
# try:
#      print("Statement-1")
#
#      try:
#          print("Statement-2")
#          print(10/0)
#      except ZeroDivisionError:
#          print("Statement-3")
#      finally:
#         print("Statement-4")
# except:
#      print("Statement-5")
# finally:
#      print("Statement-6")
#
# print("statement-7")
#
# o/p:
# Statement-1
# Statement-2
# Statement-3
# Statement-4
# Statement-6
# statement-7
#5.

# try:
#      print("Statement-1")
#
#      try:
#          print("Statement-2")
#          print(10/0)
#      except TypeError:
#          print("Statement-3")
#      finally:
#          print(10/"Ten")
#          print("Statement-4")
# except ValueError:
#      print("Statement-5")
# finally:
#      print("Statement-6")
#
# print("statement-7")
#
# o/p:
# Statement-1
# Statement-2
# Statement-6
# ZeroDivisionError
# TypeError

#6.
#
# try:
#      print("Statement-1")
#
#      try:
#          print("Statement-2")
#          print(10/0)
#      except TypeError:
#          print("Statement-3")
#      finally:
#          print(10/"Ten")
#          print("Statement-4")
# except:
#      print("Statement-5")
# finally:
#      print("Statement-6")
#
# print("statement-7")
#
# o/p:
# Statement-1
# Statement-2
# Statement-5
# Statement-6
# statement-7

# #7.
#
# try:
#      print("Statement-1")
#
#      try:
#          print("Statement-2")
#          print(10/0)
#      except TypeError:
#          print("Statement-3")
#      finally:
#          print(10/"Ten")
#          print("Statement-4")
#
# # except ZeroDivisionError: # Throw error for both. abnormal execution done.
# #     print("Erroor")
# except TypeError:  # finally block error handle. so normal execution done. we have to handle last error. otherwise throw the exception for all error.
#      print("Statement-50")
# finally:
#      print("Statement-6")
#
# print("statement-7")
#
# o/p:
# Statement-1
# Statement-2
# Statement-50
# Statement-6
# statement-7

#8.


try:
     print("Statement-1")

     try:
         print("Statement-2")
         print(10/0)
     except TypeError:
         print("Statement-3")
     finally:
         print(10/"Ten")
         print("Statement-4")

# except ZeroDivisionError: # Throw error for both. abnormal execution done.
#     print("Erroor")
except TypeError:  # finally block error handle. so normal execution done. we have to handle last error. otherwise throw the exception for all error.
     print("Statement-50")
finally:
     print("Statement-6")
     print(a)

print("statement-7")

# o/p:
# Statement-1
# Statement-2
# Statement-50
# NameError:name 'a' not defined.