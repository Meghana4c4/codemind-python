
n=int(input())
l=[]
m=[]
k=[]
for i in range(n):
    c=list(map(int,input().split()))
    l.append(c)
for i in range(n):
    c=list(map(int,input().split()))
    m.append(c)
result = [[abs(l[i][j] - m[i][j])  for j in range
(n)] for i in range(len(l))]
  
for r in result:
    print(*r)

    