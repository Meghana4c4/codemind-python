n=int(input())
l=list(map(int,input().split()))
m=len(str(abs(l[0])))
c=[]
for i in l:
    if len(str(abs(i)))>=m:
        m=len(str(abs(i)))
for i in l:
    if len(str(abs(i)))==m:
        c.append(i)
print(*c)