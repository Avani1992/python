import re
#1. with compile()
#
# count=0
# pattern=re.compile("ab")   # compile pattern in regexobject.
#
# matcher=pattern.finditer("abaababab") # Returns an Iterator object which yields Match object for every Match
#
# for match in matcher:
#     count=count+1
#     print(match.start(),"...",match.end(),"...",match.group())
#     print("The number of occurrences: ",count)

#2. without compile()

count=0
matcher=re.finditer("ab","abaababab") # Returns an Iterator object which yields Match object for every Match

for match in matcher:
    count=count+1
    print(match.start(),"...",match.end(),"...",match.group())
    print("The number of occurrences: ",count)
