cart=[10,20,600,60,70]
for item in cart:
     if item>500:
         print("To place this order insurence must be required")
         break
     elif(item==20):
         continue
     print(item)