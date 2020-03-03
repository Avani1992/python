# Write a program to find number of occurrences of each letter present in the given string?
#
# word=input("Enter the word: ")
# d=dict()
# for i in word:
#     d[i]=d.get(i,0)+1
#
# for k,v in d.items():
#      print(k,"occurred ",v," times")


# Write a program to find number of occurrences of each vowel present in the given string?

word=input("Enter the word: ")
d=dict()

v={'a','e','i','o','u'}

for i in word:
    if i in v:
        d[i]=d.get(i,0)+1

for k,v in d.items():
    print(k,"occured",v)

