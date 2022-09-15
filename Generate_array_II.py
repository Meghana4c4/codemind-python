n=int(input())
l=list(map(int,input().split()))
c=[]
for i in range(0,n,2):
    for j in range(l[i+1]):
        c.append(l[i])
print(*c)