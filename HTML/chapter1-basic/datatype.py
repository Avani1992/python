
a=10  # int
print(a)
print("Type of a: ",type(a)) # <class 'int'> # type() used to check the datatype of identifier.

b=10.25 # float
print(b)
print("Type of b: ",type(b)) #<class 'float'>

c=10+20j  # complex
print(c)
print("Real part is: ",c.real)
print("imag part is: ",c.imag)
print("Type of c: ",type(c))

d=True  # boolean
print(d)
print("Type of d: ",type(d))
print("Ans is: ",True+True+True)

e="Hello"  # string
print(e)
print("Type of e: ",type(e))

f=[10,20,30,40]  # list

g=bytes(f)  #convert list into bytes
print(g)
print(g[2])
print("Type of g: ",type(g))

#g[2]=70
#print(g[2])  # type error. bcz byte is immutable. we can't change the value...


h=bytearray(f)  # bytearray
print(h)
print(h[2])
print("Type of h: ",type(h))

h[2]=80
print(h[2])  #Ans=80. bcz bytearray is mutable. we can change the value....

l=[10,20,30,50,"Avani",10] # list insertion order maintain,hetrogeneous,mutable,duplicate allowed
print("List is: ",l)

l[3]=567.456
print("After changing: ",l)   # mutable
print("Type of l: ",type(l))
print()

t=(10,20,30,10,"Avani") # Tuple,duplicate allowed, hetrogeneous, immutable
print("Tuple is: ",t)
#t[3]=56.78
#print("After changing:",t)
print("Type of t: ",type(t))
print()


s={10,20,10,50,"Avani"} # Set duplcate not printed,insertion order not maintain, hetrogeneous,indexing not possible,mutable
print("Set is: ",s)
s.add(400)
s.remove(20)
print("After updating: ",s) # mutable
print("Type of s:",type(s))

fs=frozenset(s) # frozenset , immutable, same as set
print("Frozenset is: ",fs)
#fs.add(600)
#print("After updating: ",fs)
print("Type of fs is: ",type(fs))
print()

di={1:"Avani",2:"Kuman","Ruchi":3} # Dict. key:Value ,key is unique,value can be duplicate,mutable
print("Dict is: ",di)

di[4]="Parth"

print("after updating: ",di) # mutable
print("Type of di: ", type(di))

def a():
    return 100

print(a) # return object address

b=a()
print(b) # 100

a=input("Name:")
print(type(a))