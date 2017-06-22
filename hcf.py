x=int(input("Enter no 1"))
y=int(input("Enter no 2"))
if x>y:
    x,y=x,y
else:
    x,y=y,x
while(y):
    x,y=y,x%y
print(x)
