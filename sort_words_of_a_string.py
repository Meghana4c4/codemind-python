n=input()
q=n
n=n.split()
for i in range(len(n)):
    n[i]=sorted(n[i])
l=[]
for i in n:
    for j in i:
        l.append(j)
k='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
m=[]
a=0
for i in l:
    if i in k:
        m.append(i)

for i in range(len(q)):
    q=list(q)
    if q[i] in k:
        q[i]=m[a]
        a+=1
p=''.join(q)
print(p)