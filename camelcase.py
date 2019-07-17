"""
Alice wrote a sequence of words in CamelCase as a string of letters, , having the following properties:

It is a concatenation of one or more words consisting of English letters.
1.All letters in the first word are lowercase.
2.For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
Given ,s print the number of words in  on a new line.

For example,s="oneTwoThree" . There are 3 words in the string.
"""

s="saveChangesInTheEditor"
def camelcase(s):
  d=1
  c=1
  for i in s:
    if(i in "abcdefghijklmnopqrstuvwxyz"):
      c=1
    elif(i in  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
      d=d+1
  return (d)
result=camelcase(s)
print(result)