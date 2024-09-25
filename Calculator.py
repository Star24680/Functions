def Add(x,y):
    return x+y
def minus(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("Select an operation")
print ("Add(1)")
print ("minus(2)")
print ("multiply(3)")
print ("divide(4)")
F=int(input("Enter 1,2,3 or 4:"))
X=int(input("Enter Number 1= "))
Y=int(input("Enter number 2= "))
if F==1:
   print(X ,"+", Y,"=",Add(X,Y))
elif F==2:
    print(X ,"-", Y,"=",minus(X,Y))
elif F==3:
    print(X ,"x", Y,"=",multiply(X,Y))
else:
    print(X ,"/", Y,"=",divide(X,Y))