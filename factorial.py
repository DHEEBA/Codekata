from math import factorial
n,r=map(int,(input().split()))
f=0
for i in range(0,r+1,2):
    f=f+(factorial(n)//(factorial(i)*factorial(n-i)))
print(f)
