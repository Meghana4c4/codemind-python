def fun(n):
    s=0
    while n:
        r=n%10
        s+=r
        n=n//10
    return s
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if len(str(i))==1:
        c+=int(i)
    else:
        c+=fun(i)
print(c)
        