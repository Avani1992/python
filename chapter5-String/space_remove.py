city=input("Enter your city Name:")
#scity=city.lstrip() # remove left side space...
#scity=city.rstrip() # remove right side space...
scity=city.strip() # remove both side space...
if (scity=='Bangalore'):
     print("Hello Kannadiga...Shubhodaya")
elif (scity=='Chennai'):
       print("Hello Madrasi...Vanakkam")
elif (scity=="Hyderbad"):
       print("Hello Hyderbad People Welcome To Bangalore")
else:
     print("your entered city is invalid")