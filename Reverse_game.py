def rev(n):
    s=0
    while n:
        r=n%10
        s=s*10+r
        n=n//10
    return s
n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    d=rev(i)
    c.append(d)
print(*c)