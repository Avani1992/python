s="Learning Python is very easy"
print(s.find("Python")) #9
print(s.find("Java"))   # -1   # Java is not in String. that's why -1.
print(s.find("r"))#3
print(s.rfind("r"))#21 # rfind=right-left find. reverse side. Backward direction first 'r'

s="prasannaravipavanshiva"
print(s.find('a'))#2
print(s.find('a',8,15))#9
print(s.find('z',7,15))#-1 'z' is not in String..