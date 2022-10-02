n,m=map(int,input().split())
l=[]
k=0
for i in range(n):
    c=list(map(int,input().split()))
    l.append(c)

for i in l:
    j=sorted(i)
    if i==j or i==j[::-1]:
        k+=1
print(k)