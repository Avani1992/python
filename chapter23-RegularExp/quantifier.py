import re

#matcher=re.finditer("a","abaab%$aaabc") # exactly 'a' position
#matcher=re.finditer("a+","abaab%$aaabc") # atleast one 'a'.
#matcher=re.finditer("a*","abaab%$aaabc") # Any number of a's including zero number . for other character it's zero,
#matcher=re.finditer("a?","abaab%$aaabc") # atmost 'a'.either zero or one more no.
#matcher=re.finditer("a{2}","abaab%$aaabc") # m no. of 'a'
matcher=re.finditer("a{2,8}","abaab%$aaabc") # 2=minimum no of 'a'and 8=maximun no of 'a'.
for match in matcher:
    print(match.start(),"...",match.group())