from math import sqrt
def prime(n):
    if n==1 or n==0:
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True

n=int(input())
l=list(map(int,input().split()))
a,b,c=0,0,0
j=max(l)
k=min(l)
for i in range(n):
    if l[i]==j:
        a=i
    elif l[i]==k:
        b=i
for i in range(min(a,b),max(a,b)+1):
    if prime(l[i]):
        c+=1
print(c)
