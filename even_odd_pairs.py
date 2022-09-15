n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
k=[]
for i in l:
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
m=min(len(a),len(b))
for j in range(m):
    k.append(a[j])
    k.append(b[j])
y=abs(len(a)-len(b))
if len(a)==m:
    c=a
    d=b
else:
    c=b
    d=a
for i in range(y):
    k.append(d[m])
    m+=1
if len(k)%2:
    k.append(0)
print(*k)