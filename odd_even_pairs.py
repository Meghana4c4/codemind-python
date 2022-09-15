n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
k=[]
for i in l:
    if i%2:
        a.append(i)
    else:
        b.append(i)
m=min(len(a),len(b))
for i in range(m):
    k.append(a[i])
    k.append(b[i])
y=abs(len(a)-len(b))
if len(a)==m:
    d=b
else:
    d=a
for i in range(y):
    k.append(d[m])
    m+=1
if len(k)%2:
    k.append(0)
print(*k)