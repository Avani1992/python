# alias
x=[10,20,30,40]
y=x  # alias

y[1]=777
print(x) #[10,777,30,40] # change in y reflect to x also.
print(y) #[10,777,30,40]

# clone

x=[10,20,30,40]
y=x[:]   # slice operator for cloning..
# y=x.copy()  # copy() for cloning
y[1]=777
print(x) #[10,20,30,40] # change in y not reflect to x .
print(y) #[10,777,30,40]