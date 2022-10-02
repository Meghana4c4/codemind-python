n,m=map(int,input().split())
l=[]
s=0
for i in range(n):
    c=list(map(int,input().split()))
    l.append(c)

for i in range(n):
    for j in range(m):
        if i==j:
            s+=l[i][j]
            
for i in range(n):
    for j in range(m):
        if i+j==n-1:
            s+=l[i][j]
if n%2==0:
    print(s)
else:
    print(s-l[n-2][m-2])