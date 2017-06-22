z=int(input("Enter any number"))
s=0
while(z!=0):
    q=z//10
    r=z%10
    s=r+(s*10)
    z=q
print(s)
