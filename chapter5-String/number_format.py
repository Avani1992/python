print("The integer number is: {}".format(123)) # 123
print("The integer number is: {:d}".format(123)) # 123
print("The integer number is: {:5d}".format(123)) # __123 # 2 space after 123 # total 5 digit.
print("The integer number is: {:05d}".format(123)) # 00123 total 5 digit.

print("Float Number....")
print("The float number is: {}".format(123.4567)) # 123.4567
print("The float number is: {:f}".format(123.4567))  # 123.4567
print("The float number is: {:8.3f}".format(123.4567)) #_123.457 # total 8 digit. After '.' only 3 digit.
print("The float number is: {:08.3f}".format(123.4567)) # 0123.457
print("The float number is: {:08.3f}".format(123.45)) # 0123.450 # After ' .' 3 digit must require. so add 0 in last.
print("The float number is: {:08.3f}".format(786786123.45)) # 786786123.450