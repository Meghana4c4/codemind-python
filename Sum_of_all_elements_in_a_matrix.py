n,m=map(int,input().split())
l=[]
s=0
for i in range(n):
    k=list(map(int,input().split()))
    l.append(k)
for i in l:
    s+=sum(i)
print(s)