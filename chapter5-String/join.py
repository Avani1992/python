s={"Hello",1,2,3,4}
s1=' ' .join(str(s))
print(s1)

s2="Python is very Easy Language"
print(s2.startswith("Python")) # true
print(s2.startswith("python")) #false. python is in lowercase.
print(s2.endswith("Languag")) #false. spelling
print(s2.endswith("Language")) #True