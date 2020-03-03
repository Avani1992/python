import re

#matcher=re.finditer("[ab]","34ab$%bc") # a or b
#matcher=re.finditer("[^ab]","34ab$%bc") # except a,b everything.
#matcher=re.finditer("[A-Z]","34ab$%bCE") # capital A-Z only
#matcher=re.finditer("[0-9]","34ab$%bc8") # digit only
#matcher=re.finditer("[^a-zA-Z0-9]","34ab$%bc") # except small ,capital character and digit.i.e. special character only.

#matcher=re.finditer("\s","34ab $% bc") # space character
#matcher=re.finditer("\S","34ab $% bc") # except space character
#matcher=re.finditer("\d","34ab $% bc") # digit
#matcher=re.finditer("\D","34ab $% bc") # except digit
#matcher=re.finditer("\w","34ab $% bc") # only lowercase,uppercase,digit.
#matcher=re.finditer("\W","34ab $% bc") # except lowercase,uppercase,digit
matcher=re.finditer(".","34ab $% bc") # all things.
for match in matcher:
    print(match.start(),"  ",match.group())
