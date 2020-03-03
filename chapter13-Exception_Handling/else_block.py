#1.

# try:
#     print("Statement-1")
# except:
#     print("Statement-2")
# else:
#     print("Statement-3")
# finally:
#     print("Statement-4")

# o/p:
# Statement-1
# Statement-3
# Statement-4

# #2.
# try:
#     print("Statement-1")
#     print(10/0)
# except:
#      print("Statement-2")
# else:
#     print("Statement-3")
# finally:
#     print("Statement-4")
# o/p:
# Statement-1
# Statement-2
# Statement-4

#3.
try:
    print("try")
except :
    print("except")
print("Hello")
# except: # syntax error..
#     print("hi")
# finally: # syntax error..
#     print("Finally..")

#4.
try:
    print("try")
except:
    print("except")
if 10>20:
    print("if")
else:
    print("else")
#5.

# try:
#     print("stmt-1")
#     try:
#         print("stmt-2") # if we don't write except in nested try it gives syntax error for except or finally...
# except:
#     print("stmt-3")

x=int("Ten")
print(x) # value error.

