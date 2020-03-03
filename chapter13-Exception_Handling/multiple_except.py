#1.
# try:
#      x=int(input("Enter First Number: "))
#      y=int(input("Enter Second Number: "))
#      print(x/y)
# except ArithmeticError :  # Raise the parent error if it first.
#      print("ArithmeticError")
# except ZeroDivisionError :
#      print("ZeroDivisionError")
# except ValueError:
#     print("ValueError")

#o/p:
# Enter First Number: 10
# Enter Second Number: 0
# ArithmeticError

print()
#2.

# try:
#      x=int(input("Enter First Number: "))
#      y=int(input("Enter Second Number: "))
#      print(x/y)
# except (ZeroDivisionError,ValueError) as msg:
#      print("Plz Provide valid numbers only and problem is: ",msg)

# print()
# 3.

# try:
#     x = int(input("Enter First Number: "))
#     y = int(input("Enter Second Number: "))
#     print(x / y)
# except (ZeroDivisionError) as msg:
#     print("Plz Provide valid numbers only and problem is: ", msg)
# except:
#     print("Enter valid input...") # exception other than Zerodivision Error .except execute.
#
#o/p:
# Enter First Number: 10
# Enter Second Number: Ten
# Enter valid input...

print()

#4.

try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    print(x / y)
# except:
#     print("Enter valid input...") # default 'except' must be last. Default except only write after all except condition with error.
except (ZeroDivisionError) as msg:
    print("Plz Provide valid numbers only and problem is: ", msg)





