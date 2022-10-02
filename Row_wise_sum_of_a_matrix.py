n,m=map(int,input().split())
l=[]
k=[]
for i in range(n):
    c=list(map(int,input().split()))
    l.append(c)
for i in l:
    k.append(sum(i))
print(*k)