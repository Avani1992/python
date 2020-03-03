 #1.

for i in range(10):
   if i%2==0:
         continue
   print(i)

print()
print()

 #2.

cart = [10, 20, 500, 700, 50, 60]
for item in cart:
    if item >= 500:
        print("We cannot process this item :", item)
        continue
    print(item)
print()
print()

#3.

numbers=[10,20,0,5,0,30]
for n in numbers:
     if n==0:
         print("Hey how we can divide with zero..just skipping")
         continue
     print("100/{} = {}".format(n,100/n))